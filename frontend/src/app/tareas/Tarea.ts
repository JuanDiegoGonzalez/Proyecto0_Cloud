export class Tarea {
    constructor(public texto:string,
        public fecha_creacion:Date,
        public fecha_tentativa_finalizacion:Date,
        public estado:any,
        public estado_display:string,
        public usuario:number,
        public categoria:number,
        public categoria_display:string) {
            
        }
}