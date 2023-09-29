Author: Austine Abine

# Python - Network #0

In the course of this networking project, I leveraged the 'curl' utility within Bash scripts to dispatch a diverse array of HTTP headers. Throughout this endeavor, I acquired valuable insights into the intricate workings of URLs, domain naming conventions, the multifaceted landscape of HTTP request and response header fields, status codes, as well as proficient techniques for managing cookies.

Additionally, it is noteworthy that Task six represented a distinct algorithmic challenge, distinct from the overarching project theme, and was successfully implemented using the Python programming language.

## Tasks :page_with_curl:

**Note:** The `curl` behavior in all Bash scripts was designed to interact with a
server set up in a container.

* **0. cURL body size**
  - [0-body_size.sh](./0-body_size.sh): A Bash script that sends a `GET` request to
  a specified URL and displays the size of the response body in bytes.

* **1. cURL to the end**
  - [1-body.sh](./1-body.sh): A Bash script that sends a `GET` request to a specified
  URL and displays the response body for a `200` status code response.

* **2. cURL Method**
  - [2-delete.sh](./2-delete.sh): A Bash script that sends a `DELETE` request to a specified
  URL and displays the response body.

* **3. cURL only methods**
  - [3-methods.sh](./3-methods.sh): A Bash script that displays all HTTP methods
  accepted by the server of a specified URL.

* **4. cURL headers**
  - [4-header.sh](./4-header.sh): A Bash script that sends a `GET` request to a
  specified URL with a header variable `X-HolbertonSchool-User-Id=98` and displays
  the response body.

* **5. cURL POST parameters**
  - [5-post_params.sh](./5-post_params.sh): A Bash script that sends a `POST`
  request to a specified URL with the variables `email=test.gmail.com` and
  `subject=I will always be here for PLD` and displays the response body.

* **6. Find a peak**
  - [6-peak.py](./6-peak.py): A Python program for [technical interview preparation] that finds a peak in a list of unsorted integers.
  - [6-peak.txt](./6-peak.txt): A text file containing the complexity of the
  algorithm.

* **7. Only status code**
  - [100-status_code.sh](./100-status_code.sh): A Bash script that sends a `GET`
  request to a specified URL without using pipes, redirections, `;`, or `&&`, and
  displays the status code of the response.

* **8. cURL a JSON file**
  - [101-post_json.sh](./101-post_json.sh): A Bash script that sends a JSON `POST`
  request with the contents of a provided file to a specified URL and displays the
  response body.

* **9. Catch me if you can!**
  - [102-catch_me.sh](./102-catch_me.sh): A Bash script that sends a request to
  `0.0.0.0:5000/catch_me`, causing the server to respond with a message
  containing `You got me!` in the response body.

## Summary
The code snippet 'Code-Under-Test' is a part of a networking project implemented in Python. It includes several Bash scripts and a Python program. The Python program, '6-peak.py', is an algorithmic challenge that finds a peak in a list of unsorted integers.

## Code Analysis

### Inputs
The input for the 'find_peak' function is a list of unsorted integers.
___
### Flow
1. The 'find_peak' function takes a list of unsorted integers as input.
2. It uses a divide-and-conquer approach to find a peak element in the list.
3. The function compares the middle element of the list with its neighbors to determine if it is a peak.
4. If the middle element is not a peak, the function recursively calls itself on the half of the list that contains the larger neighbor of the middle element.
5. The function continues this process until a peak element is found or the list is reduced to a single element.
___
### Outputs
The output of the 'find_peak' function is the peak element in the list of unsorted integers.
___
### Complexity
The complexity of the 'find_peak' function is O(log(n)).
___