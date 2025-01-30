import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

function ClubEvents() {
  return (
    <div>
      <Header />
      <div className="p-4">
        <h1 className="text-2xl font-bold mb-4">Club Events</h1>
        <p>Join and participate in various club events.</p>
      </div>
      <Footer />
    </div>
  );
}

export default ClubEvents; 