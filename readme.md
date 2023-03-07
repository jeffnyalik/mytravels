## MyTravels
This is a booking and management system that allows travel agencies to manage their bookings, inventory, payments, and customer feedback efficiently.
It is  designed to cater to the needs of small and large travel agencies, tour operators, and travel management companies.
The system has 3 types of users: customers, vendors/suppliers and administrators. Customers use the system to browse and book travel services, while administrators use it to manage bookings, inventory, payments, and customer feedback,vendors/suppliers
can post their services and get a commission as per booking.
The project uses Python and the Django framework. Users can browse available rooms, view details about a room, and book a room for a specific date range.

## Features
User authentication (login and registration)
User profile management (view and update profile information)
Search functionality (search for rooms based on location and date range)
Booking functionality (book a room for a specific date range)
Admin panel (manage rooms, bookings, and users)
Vendor panel(manage services i.e hotels and flights)

Installation
Clone the repository
bash
Copy code
git clone https://github.com/jeffnyalik/mytravels.git
Install dependencies
bash
Copy code
pip install -r requirements.txt
Create a .env file and set your environment variables (see .env.example for an example)

Run database migrations

bash
Copy code
python manage.py migrate
Create a superuser (admin)
bash
Copy code
python manage.py createsuperuser
Run the server
bash
Copy code
python manage.py runserver
Open your browser and go to http://localhost:8000 to view the website
Usage
Admin Panel
To access the admin panel, go to http://localhost:8000/admin and login with your admin credentials.

Searching for Rooms
On the homepage, users can search for rooms based on location and date range.

Booking a Room
Click on a room to view its details
Select a check-in date and check-out date
Click the "Book Now" button
Enter your payment information and click "Submit"
User Profile
Users can view and update their profile information by clicking on the "Profile" link in the navbar.

Contributing
Contributions are welcome! If you have any suggestions or would like to report a bug, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more information.