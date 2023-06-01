import requests


def send_requests():
    # send requests
    print("##### HERE WE SEND A GET REQUEST #####")
    r = requests.get("http://localhost:5000/endpoint_to_get?name=John&name=Mary&age=20")
    print(r.json())

    print("##### HERE WE SEND A POST REQUEST WITH JSON #####")
    r = requests.post(
        "http://localhost:5000/endpoint_to_post_json",
        json={"name": "John", "age": 20}
    )
    print(r.json())

    print("##### HERE WE SEND A POST REQUEST WITH DATA AND FILES #####")
    # here some how we cannot add json={} for flask to request.json
    # will end up 400
    r = requests.post(
        "http://localhost:5000/endpoint_to_post_data_and_files",
        data={"name": "John", "age": 20},
        files={"file_xxx": open("ship.jpg", "rb")},
    )
    print(r.json())


if __name__ == "__main__":
    send_requests()