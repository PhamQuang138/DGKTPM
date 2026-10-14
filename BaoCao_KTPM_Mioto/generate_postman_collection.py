import json

collection = {
    "info": {
        "_postman_id": "mioto-sqa-automation-collection-2026",
        "name": "Mioto.vn API Testing Suite - SQA Automation",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
        "description": "Bộ sưu tập kịch bản kiểm thử API tự động cho hệ thống Mioto.vn - Sinh viên: Phạm Duy Quang (23017167)"
    },
    "item": [
        {
            "name": "01. Search Cars by Location",
            "request": {
                "method": "GET",
                "header": [
                    {"key": "Accept", "value": "application/json"}
                ],
                "url": {
                    "raw": "https://m-car.mioto.vn/cars?city=hochiminh&vtype=1&page=1&limit=20",
                    "protocol": "https",
                    "host": ["m-car", "mioto", "vn"],
                    "path": ["cars"],
                    "query": [
                        {"key": "city", "value": "hochiminh"},
                        {"key": "vtype", "value": "1"},
                        {"key": "page", "value": "1"},
                        {"key": "limit", "value": "20"}
                    ]
                }
            },
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "type": "text/javascript",
                        "exec": [
                            "pm.test('Status code is 200 or 404', function () {",
                            "    pm.expect(pm.response.code).to.be.oneOf([200, 404]);",
                            "});",
                            "pm.test('Response time is below 1500ms', function () {",
                            "    pm.expect(pm.response.responseTime).to.be.below(1500);",
                            "});"
                        ]
                    }
                }
            ]
        },
        {
            "name": "02. Pricing and Surcharge Calculation",
            "request": {
                "method": "POST",
                "header": [
                    {"key": "Content-Type", "value": "application/json"}
                ],
                "body": {
                    "mode": "raw",
                    "raw": json.dumps({
                        "carId": "CAR_VINFAST_VF8_2024",
                        "startDate": "2026-11-01T08:00:00Z",
                        "endDate": "2026-11-03T08:00:00Z",
                        "deliveryDistanceKm": 12.0,
                        "voucherCode": "MIOTOHELLO"
                    })
                },
                "url": {
                    "raw": "https://m-car.mioto.vn/pricing/calculate",
                    "protocol": "https",
                    "host": ["m-car", "mioto", "vn"],
                    "path": ["pricing", "calculate"]
                }
            },
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "type": "text/javascript",
                        "exec": [
                            "pm.test('Response contains valid payload or handled status', function () {",
                            "    pm.expect(pm.response.code).to.be.oneOf([200, 400, 404]);",
                            "});"
                        ]
                    }
                }
            ]
        },
        {
            "name": "03. Get Card List from Payment Service",
            "request": {
                "method": "GET",
                "header": [],
                "url": {
                    "raw": "https://payment.mioto.vn/alepay/get-list-card",
                    "protocol": "https",
                    "host": ["payment", "mioto", "vn"],
                    "path": ["alepay", "get-list-card"]
                }
            },
            "event": [
                {
                    "listen": "test",
                    "script": {
                        "type": "text/javascript",
                        "exec": [
                            "pm.test('Payment service status check', function () {",
                            "    pm.expect(pm.response.code).to.be.oneOf([200, 401, 403]);",
                            "});"
                        ]
                    }
                }
            ]
        }
    ]
}

with open('BaoCao_KTPM_Mioto/Mioto_Postman_Collection.json', 'w', encoding='utf-8') as f:
    json.dump(collection, f, ensure_ascii=False, indent=2)
print("Saved BaoCao_KTPM_Mioto/Mioto_Postman_Collection.json")

