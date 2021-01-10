import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PredictService {
  //URL to flask API
  url_base = "http://localhost:5000/api/"

  constructor(private http: HttpClient) { }

  predictImage(image) {
    const formData = new FormData();
    formData.append('image', image);

    return this.http.post(`${this.url_base}predict`, formData);
  }
}
