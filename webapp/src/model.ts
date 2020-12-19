
export enum StatusEnum {
    TODO = "TODO",
    DOING = "DOING",
    DONE = "DONE"
}

export class Todo {
    id: number;
    title: string;
    description: string
    status: StatusEnum 

    constructor(id: number, title: string, description: string, status: StatusEnum) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.status = status;
    }

}