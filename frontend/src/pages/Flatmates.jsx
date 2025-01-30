import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

function Flatmates() {
  return (
    <div>
      <Header />
      <div className="p-4">
        <h1 className="text-2xl font-bold mb-4">Find Flatmates</h1>
        <p>Connect with students for shared accommodation.</p>
      </div>
      <Footer />
    </div>
  );
}

export default Flatmates; 