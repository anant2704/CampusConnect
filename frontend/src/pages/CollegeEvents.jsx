import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

function CollegeEvents() {
  return (
    <div>
      <Header />
      <div className="p-4">
        <h1 className="text-2xl font-bold mb-4">College Events</h1>
        <p>Participate in college activities and events.</p>
      </div>
      <Footer />
    </div>
  );
}

export default CollegeEvents; 