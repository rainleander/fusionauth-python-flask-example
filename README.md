# FusionAuth Python Flask Example

This example demonstrates how to integrate [FusionAuth](https://fusionauth.io/) with a [Python Flask application](https://flask.palletsprojects.com/en/2.3.x/) using [OAuth 2.0](https://oauth.net/2/). It includes features such as login, displaying user profile information, and logout functionality.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [FusionAuth installed](https://fusionauth.io/docs/v1/tech/installation-guide/) and configured (either on your local machine or using the cloud version)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/rainleander/fusionauth-python-flask-example.git
cd fusionauth-python-flask-example
```

2. Install the required Python libraries:

```bash
pip install flask requests
```

3. Configure your FusionAuth credentials:

Open `app.py` and replace the following placeholders with the appropriate values from your FusionAuth instance:

- `'your_client_id'`
- `'your_client_secret'`
- `'https://your_fusionauth_url'`

Make sure to replace `'your_secret_key'` with a secure secret key for Flask.

4. Run the application:

```bash
python app.py
```

5. Test the application:

Open your browser and navigate to http://localhost:5000. You should see a "Login with FusionAuth" link. Click on it to log in or register a new user. After successful authentication, you should be redirected to the profile page displaying the user's information.

## Features

- Login with FusionAuth using OAuth 2.0
- Display user profile information
- Logout functionality

## Contributing

Thank you for your interest in contributing to this project! We welcome and appreciate contributions from the community. Here's how you can get involved:

1. **Fork** the repository on GitHub by clicking the _Fork_ button in the top right corner.

2. **Clone** the forked repository to your local machine:

```bash
git clone https://github.com/your_username/fusionauth-python-flask-example.git
cd fusionauth-python-flask-example
```

3. **Create a new branch** for your feature or bug fix:

```bash
git checkout -b your_feature_branch
```

4. **Make your changes** in the new branch, and ensure that your code is well-organized, follows best practices, and includes comments where necessary.

5. **Test** your changes by running the application and ensuring everything works as expected.

6. **Commit** your changes with a clear and descriptive commit message:

```bash
git commit -m "Add a brief description of your changes"
```

7. **Push** your changes to your fork on GitHub:

```bash
git push origin your_feature_branch
```

8. **Create a pull request** by navigating to your forked repository on GitHub, switching to your feature branch, and clicking the _New Pull Request_ button.

9. **Describe your changes** in the pull request, and submit it.

After submitting your pull request, the project maintainers will review your changes. They may ask for additional changes or clarification before merging your changes. Remember to be patient and respectful during the review process, as the maintainers are volunteering their time to maintain this project.

Once again, thank you for your interest in contributing to the FusionAuth Python Flask Example. We look forward to collaborating with you and creating a better experience for the community!

## License

This project is licensed under the Apache 2.0 License.
