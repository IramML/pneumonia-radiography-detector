export class Prediction {
    constructor(code='', message='', prediction=''){
        this.code=code;
        this.message=message;
        this.prediction=prediction;
    }
    code: string;
    message: string;
    prediction: string;
}
