import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

function Login() {
  return (
    <div>
      <Header />
      <div className="p-4">
        <h1>Login Page</h1>
        <p>This is the login page.</p>
      </div>
      <Footer />
    </div>
  );
}

export default Login; 