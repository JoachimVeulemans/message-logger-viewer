import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
    providedIn: 'root'
})
export class ApiService {
    private API_URL = environment.apiUrl;
    private optionsWithJSON = {headers: new HttpHeaders({'Content-Type': 'application/json'})};

    constructor(private http: HttpClient) { }

    getAllLogs(): Observable<any[]> {
        const url = `${this.API_URL}/logs`;
        return this.http.get<any[]>(url, this.optionsWithJSON);
    }

    clearAllLogs(): Observable<any> {
        const url = `${this.API_URL}/logs`;
        return this.http.delete<any>(url, this.optionsWithJSON);
    }
}
