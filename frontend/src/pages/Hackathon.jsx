import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

function Hackathon() {
  return (
    <div>
      <Header />
      <div className="p-4">
        <h1 className="text-2xl font-bold mb-4">Nirmaan Hackathon 2023</h1>
        <p className="mb-2">Join us for an exciting hackathon where innovation meets creativity!</p>
        <ul className="list-disc pl-5">
          <li>Date: December 10-12, 2023</li>
          <li>Location: Virtual</li>
          <li>Theme: Building Sustainable Solutions</li>
          <li>Prizes: ₹10,000 in total prizes</li>
          <li>Registration Deadline: November 30, 2023</li>
        </ul>
        <p className="mt-4">For more details, visit our website or contact us at hackathon@nirmaan.com.</p>
      </div>
      <Footer />
    </div>
  );
}

export default Hackathon; 