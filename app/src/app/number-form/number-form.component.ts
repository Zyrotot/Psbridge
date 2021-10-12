import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-number-form',
  templateUrl: './number-form.component.html',
  styleUrls: ['./number-form.component.css']
})

export class NumberFormComponent{

  numberForm = this.fb.group({
    number: ['', Validators.required],
  });

  show: string = '';

  constructor(private fb: FormBuilder, private http: HttpClient) {
    this.show = ''
   }

   get getshow() {
    return this.show;
  }

  onSubmit(): void {
    console.warn('Your order has been submitted', this.numberForm.value);

    var data = this.numberForm.value
    var values = JSON.stringify(data)

    let headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': 'localhost',
    })

    let options = { headers: headers};
  
    this.http.post('http://localhost:5000/', values, options).subscribe(
      result => this.show = JSON.stringify(result)
    )
  }
}
