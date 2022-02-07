
### Prerequisites

You need to install docker to run docker commands
* Docker
  ```sh
  https://www.docker.com/get-started
  ```

* After you download repo, in root folder run:
  ```sh
    Docker-compose run
  ```

### End-Points

* Api Root
  ```sh
    http://localhost:8000/
  ```
    
#### Question 1

*  End-point
    ```sh
     http://localhost:8000/last-points/
   ```
* This end-point return list of navigation records. I used '__range' to filter last records in 48 hours.


* 'startswith' also can be used (it compares by matching char by char to filter).


* Timescale DB can also be used, because that have options to perform queries according to time.


#### Question 2

  ```sh
  http://localhost:8000/last-points/
  ```