from flask import Flask, redirect, request, session, url_for
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Replace these with your FusionAuth credentials
client_id = 'YOU_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
fusionauth_url = 'https://YOUR_FUSIONAUTH_URL'

@app.route('/')
def home():
    return '''
    <a href="/login">Login with FusionAuth</a>
    '''

@app.route('/login')
def login():
    authorize_url = f'{fusionauth_url}/oauth2/authorize?client_id={client_id}&response_type=code&redirect_uri=http://localhost:5000/callback'
    return redirect(authorize_url)

@app.route('/logout')
def logout():
    session.pop('access_token', None)
    return redirect(url_for('home'))

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_url = f'{fusionauth_url}/oauth2/token'
    token_data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://localhost:5000/callback'
    }
    response = requests.post(token_url, data=token_data)
    response_json = response.json()
    session['access_token'] = response_json['access_token']

    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    access_token = session['access_token']
    userinfo_url = f'{fusionauth_url}/oauth2/userinfo'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(userinfo_url, headers=headers)
    user_info = response.json()

    return f'''
    <h1>Welcome, {user_info["given_name"]} {user_info["family_name"]}</h1>
    <pre>{user_info}</pre>
    <a href="/logout">Logout</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
