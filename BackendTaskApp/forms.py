import requests
import json
from flask_wtf import FlaskForm


class DataHandleForm(FlaskForm):
    base_url = "https://api-dev.massbio.info/assignment/"
    query = "SELECT * FROM public.report_output"
    
    page = None
    page_size = None
    is_paginate = None
    is_order_by = None 
    is_filter = None
    
    def __init__(self, *args, **kwargs):
        super(DataHandleForm, self).__init__(*args, **kwargs)
        self.error_code = None
        self.form_error = ''
    
    def _headers(self):
        return {'Content-Type': 'application/json'}
    
    def _make_json_request(self, _url, data):
        response = requests.post(url=_url, json=data, headers=self._headers(), verify=False)
        try:
            if 199 < response.status_code < 300:
                return True, response.json()
        except Exception as e:
            self.form_error = e
            return False
        return False, str(response.content)
    
    def pagination(self):
        pagination_url = f"{self.base_url}{self.query}/page={self.page}&/page_size={self.page_size}"
        request_data = {}
        success, data = self._make_json_request(pagination_url, request_data)
        if not success:
            return False, data 
        return success, data
    
    def filtering(self):
        filter_url = f"{self.base_url}{self.query}"
        request_data = {"filters": {'main_dp': 277}}
        success, data = self._make_json_request(filter_url, request_data)
        if not success:
            return False, data 
        return success, data

    def ordering(self):
        ordering_url = f"{self.base_url}{self.query}"
        request_data = {"ordering": [{"name": "ASC"}]}
        success, data = self._make_json_request(ordering_url, request_data)
        if not success:
            return False, data 
        return success, data

    def perform(self):
        if self.is_paginate:
            self.pagination()
        elif self.is_filter:
            self.filtering()
        elif self.is_order_by:
            self.ordering()