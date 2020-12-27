import { io } from "socket.io-client"
import { Todo } from "./model"

const socketio = io("ws://localhost:5000/boards")

export function onConnect(fn) {
    socketio.on('connect', fn)
} 

export function subscribeToBoard(id: number, fn: (Todo) => void) {
    socketio.emit('board_subscribe', { id: id })

    socketio.on('board_update', 
        ({ id, title, description, status }) => fn(new Todo(id, title, description, status))
    )
}