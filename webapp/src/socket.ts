import { io } from "socket.io-client"

const socketio = io("ws://localhost:5000/boards")

export function onConnect(fn) {
    socketio.on('connect', fn)
} 

export function subscribeToBoard(id, fn) {
    socketio.emit('board_subscribe', { id: id })

    socketio.on('board_update', fn)
}