# Catalog Handbook Application
This is prototype for a catalog handbook.


## Getting Started
### Installation 
Install and configure the VM following the [instruction](https://github.com/udacity/fullstack-nanodegree-vm). 

### Get VM up and running
After navigating to the directory that the VM file are stored, run `vagrant up` and `vagrant ssh` to get the VM up and running. More detail see [Udacity Full Stack VM - start the virtual machine](https://github.com/udacity/fullstack-nanodegree-vm#start-the-virtual-machine)
If you have trouble with VM set up and running, refer to [Udacity Full Stack VM - troubleshooting](https://github.com/udacity/fullstack-nanodegree-vm#start-the-virtual-machine)

## Running the test
### 1.Lauch vagrant
After navigating to the directory of `Vagrantfile`, start the VM by running following commands:
```
vagrant up
vagrant ssh
```

### 2. Create Database
Navigate to the directory of `database_setup.py`, run the command:
```
python3 database_setup.py
```

### 3. Populate Data in the Database
Run the command:
```
python3 lotsofitem.py
```

### 4. Launch the Flask Application
Run the command:
```
python3 catelog.py
```

### 5. Browsing Experience
Start the browsing experience by visiting `http://0.0.0.0:5000/` in your browser.

### 6. Visit API Endpoint
API endpoint is available for items in each category by visiting `/<category_name>/JSON/`
Example output:
```json

{
  "item": [
    {
      "category_id": 1,
      "description": "Snowboard boots are designed to conform to your feet specifically",
      "id": 1,
      "name": "Boots",
      "timestamp": "Sun, 01 Dec 2019 08:15:10 GMT"
    },
    {
      "category_id": 1,
      "description": "Snowboard socks are essential because cold feet will quickly ruin your day.",
      "id": 2,
      "name": "Snowboard Socks",
      "timestamp": "Sun, 01 Dec 2019 08:15:10 GMT"
    }
  ]
}
```


## Author
- Yuhuan Fan 

## Supporting Materials
- [Full Stack Web Developer Nanodegree program virtual machine](https://github.com/udacity/fullstack-nanodegree-vm#full-stack-web-developer-nanodegree-program-virtual-machine)
