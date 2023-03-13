curl --location --request GET 'http://localhost:5000/endpoint_to_get?x=1&y=2'

# {
#   "the-args": {
#     "x": "1",
#     "y": "2"
#   }
# }


curl --location --request POST 'http://localhost:5000/endpoint_to_post_json' \
--header 'Content-Type: application/json' \
--data-raw '{"x": 1, "y": 2}'

# {
#     "the-json": {
#         "x": 1,
#         "y": 2
#     }
# }

curl --location --request POST 'http://localhost:5000/endpoint_to_post_data_and_files' \
--form 'x="1"' \
--form 'y="2"' \
--form 'file1=@"/Users/yijun/Downloads/ship1.jpg"'
# change the absolute path to your own path


# {
#     "the-files": {
#         "file1": "/var/folders/z7/_b9x2x8d4ndffpfrvmq6zssc0000gn/T/tmpeuz8lygc1678679867.79342/ship1.jpg"
#     },
#     "the-form": {
#         "x": "1",
#         "y": "2"
#     }
# }



