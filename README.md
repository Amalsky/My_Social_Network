My Social Network
My Social Network is a web application that allows users to connect with friends, share updates, and explore content in a social media-like environment. It is built using Django, CSS, and JavaScript.

Key Features
User Registration: Users can create an account by providing their username, email, and password.
User Profile: Each user has a profile page where they can upload a profile picture and update their information.
Post Creation: Users can create new posts by providing a title and content.
Post Listing: The home page displays a list of posts in reverse chronological order.
Post Detail: Users can view the full details of a post by clicking on its title.
Post Update and Delete: Users can edit and delete their own posts.
User Posts: Users can view a list of posts created by a specific user.
Favourites: Users can add posts to their favourites list.

Installation
Clone the repository:
git clone https://github.com/Amalsky/My_Social_Network
Navigate to the project directory:
cd my-social-network
Create a virtual environment:
python3 -m venv env
Activate the virtual environment:
For Mac/Linux:
source env/bin/activate
For Windows:
env\Scripts\activate
Install the dependencies:
pip install -r requirements.txt
Apply the database migrations:
python manage.py migrate
Run the development server:
python manage.py runserver
Open your browser and navigate to http://localhost:8000 to access the application
Usage
Register a new account by clicking on the "Register" link on the home page.
Log in with your account credentials.
Explore the home page to see the latest posts from all users.
Click on a post title to view its details.
On your profile page, you can update your profile picture and other information.
Create a new post by clicking on the "New Post" link.
Edit or delete your own posts by navigating to the post detail page and clicking on the respective buttons.
View posts by a specific user by clicking on their username on the home page or using the URL pattern /user/<username>.
Add posts to your favourites list by clicking on the "Add to Favourites" button on the post detail page.
View your favourite posts by navigating to the "Favourites" page.
API Endpoints
The application also provides several API endpoints for programmatic access to the data. Here are some key endpoints:

Authentication:

/api-auth/: API authentication endpoints.
User:

/api/user/signup/: User signup API for creating new users and listing user details.
Posts:

/api/post_create_list/: Post creation and listing API (authentication required for post creation).
/api/post/detail/<int:pk>/: Post detail API for retrieving a specific post.
/api/post/update/<int:pk>/: Post update API for editing a post (authentication and ownership required).
/api/post/delete/<int:pk>/: Post deletion API for deleting a post (authentication and ownership required).
/api/post/user/<int:author_id>/: List posts by a specific author.
Profile:

/api/profile_create_list/: Profile creation and listing API (authentication required).
/api/profile/update/: Profile update API for editing the profile (authentication and ownership required).
For detailed API documentation, please refer to the API documentation or consult the developers' guide.

Contributing
Contributions are welcome! If you find any issues or want to add new features, please submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.



Contact
For any inquiries or support, please contact amalsky05@gmail.com.












