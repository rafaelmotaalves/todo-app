import axios from "axios"
import { StatusEnum, Todo } from "./model"

const client = axios.create({
    baseURL: 'http://localhost:5000'
})

export async function getAllTodos(): Promise<Todo[]> {
    const res = await client.get("/todos")

    return res.data.map(
        ({ id, title, description, status }) => new Todo(id, title, description, status)
    )
} 

export async function updateStatus(todoId: number, status: StatusEnum) {
    const res = await client.put(`/todos/${todoId}`, { status })

    return res.data;
}
