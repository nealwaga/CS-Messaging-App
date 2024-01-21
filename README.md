# CS-Messaging-App

## Built By [Neal Waga](https://github.com/nealwaga/)

## SetUp / Installation Requirements
### Cloning
* In your terminal:

    >``$ git clone https://github.com/nealwaga/CS-Messaging-App``
    >``$ cd CS-Messaging-App``

### Running the Application
After extracting the files,
1. Stop postgres
>`` sudo systemctl stop postgresql.service ``
2. Create a file named .env.dev in the base directory
>`` touch .env.dev ``
3. Copy the details in the file .env.example file into the .env.dev file
4. Build and start the application for initial setup
>`` docker compose up --build ``
5. Start the application without building (for continuous development)
>`` docker compose up``

### Django Management
1. `` docker exec -it <backend_service_name> python manage.py makemigrations ``
2. `` docker exec -it <backend_service_name> python manage.py migrate ``

### Installating CSV File Data
When the application is running, open a new terminal,
>`` docker ps ``
> `` docker exec -it <backend_service_name> bash ``
> `` python manage.py shell ``
> `` import save_data ``