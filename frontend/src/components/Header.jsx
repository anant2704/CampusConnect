import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header
      style={{
        backgroundColor: '#333',
        color: 'white',
        padding: '10px 20px',
        textAlign: 'center',
      }}
    >
      <h1>
        <Link to="/" style={{ color: 'white', textDecoration: 'none' }}>
          Campus Connect
        </Link>
      </h1>
    </header>
  );
}

export default Header; 