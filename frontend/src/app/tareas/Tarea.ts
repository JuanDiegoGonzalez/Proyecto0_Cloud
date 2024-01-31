export class Tarea {
    constructor(public texto:string,
        public fecha_creacion:Date,
        public fecha_tentativa_finalizacion:Date,
        public estado:string,
        public usuario:number,
        public categoria:number) {
            
        }
}