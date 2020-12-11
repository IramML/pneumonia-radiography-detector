import { Component, OnInit } from '@angular/core';
import { Prediction } from 'src/app/models/prediction.model';
import { PredictService } from 'src/app/services/predict.service';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.scss']
})
export class PredictComponent implements OnInit {

  imagePath;
  imgURL: any;
  message: string;
  prediction: String;
  isFetching = false;

  fileImage;

  constructor(private predictService: PredictService) { }

  ngOnInit(): void { }
 
  preview(files) {
    this.fileImage = files[0];
    if (files.length === 0)
      return;
 
    const mimeType = files[0].type;
    if (mimeType.match(/image\/*/) == null) {
      this.message = "Only images are supported.";
      return;
    }
 
    const reader = new FileReader();
    this.imagePath = files;
    reader.readAsDataURL(files[0]); 
    reader.onload = (_event) => { 
      this.imgURL = reader.result; 
    }
  }

  predict() {
    if (this.fileImage == undefined)
    return;
    this.isFetching = true;
    this.prediction = "";
    this.predictService.predictImage(this.fileImage)
      .subscribe((prediction: Prediction) => {
        this.isFetching = false;
        this.prediction = prediction.prediction;
      }, error => {
        this.isFetching
      });
  }

}
