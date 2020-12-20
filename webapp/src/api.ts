import axios from "axios"
import { Board, StatusEnum, Todo } from "./model"

const client = axios.create({
    baseURL: 'http://localhost:5000'
})

export async function getBoards() {
    const res = await client.get("/boards");

    return res.data.map(
        ({ title, id }) => new Board(id, title, [])
    )
}

export async function getBoardWithTodos(boardId: number) {
    const boardPromise = client.get(`/boards/${boardId}`);
    const todosPromise = getAllTodos(boardId)

    const todos = await todosPromise;
    const board = await boardPromise;

    return new Board(board.data.id, board.data.title, todos)
}

export async function getAllTodos(boardId: number): Promise<Todo[]> {
    const res = await client.get(`/boards/${boardId}/todos`)

    return res.data.map(
        ({ id, title, description, status }) => new Todo(id, title, description, status)
    )
} 

export async function updateStatus(boardId: number, todoId: number, status: StatusEnum) {
    const res = await client.put(`/boards/${boardId}/todos/${todoId}`, { status })

    return res.data
}

export async function createTodo(boardId: number,  title: string, description: string) {
    const res = await client.post(`/boards/${boardId}/todos`, { title, description })

    return res.data
}
