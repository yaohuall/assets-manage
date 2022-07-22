import request from "./request"

export default class APIBase{
    public name: string;

    constructor(name:string){
        this.name = name
    }

    public getData = (params?: any) => {
        return request({
            method:'get',
            url:`${this.name}/`,
            params
        })
    }
    public addData = (data: any) => {
        // request
        return request({
            method: 'post',
            url: `${this.name}/`,
            data
        })
    }
    public del = (id: any) =>{
        // request请求
        return request({
            method: 'delete',
            url: `${this.name}/${id}/`,
      
        })
    }
}

