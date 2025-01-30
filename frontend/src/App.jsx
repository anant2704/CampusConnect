import React from 'react';
import { Routes, Route, useNavigate } from 'react-router-dom';
import Hackathon from './pages/hackathon';
import Login from './pages/login';
import Flatmates from './pages/flatmates';
import CollegeEvents from './pages/collegeevents';
import ClubEvents from './pages/clubevents';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/hackathon" element={<Hackathon />} />
      <Route path="/login" element={<Login />} />
      <Route path="/flatmates" element={<Flatmates />} />
      <Route path="/college-events" element={<CollegeEvents />} />
      <Route path="/club-events" element={<ClubEvents />} />
    </Routes>
  );
}

function Home() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        fontFamily: "Arial, sans-serif",
        backgroundColor: "#f4f4f4",
        textAlign: "center",
        padding: "20px",
        minHeight: "100vh",
      }}
    >
      <div
        style={{
          maxWidth: "800px",
          margin: "auto",
          background: "white",
          padding: "20px",
          borderRadius: "10px",
          boxShadow: "0 0 10px rgba(0, 0, 0, 0.1)",
        }}
      >
        <h1 style={{ color: "#333" }}>Campus Connect</h1>
        <div
          style={{
            display: "flex",
            justifyContent: "space-around",
            flexWrap: "wrap",
          }}
        >
          <div
            style={{
              width: "250px",
              padding: "20px",
              background: "#007BFF",
              color: "white",
              borderRadius: "10px",
              margin: "10px",
              cursor: "pointer",
            }}
            onClick={() => navigate("/hackathon")}
          >
            <h2>Hackathon Groups</h2>
            <p>Find and join teams for hackathons.</p>
          </div>
          <div
            style={{
              width: "250px",
              padding: "20px",
              background: "#28A745",
              color: "white",
              borderRadius: "10px",
              margin: "10px",
              cursor: "pointer",
            }}
            onClick={() => navigate("/flatmates")}
          >
            <h2>Find Flatmates</h2>
            <p>Connect with students for shared accommodation.</p>
          </div>
          <div
            style={{
              width: "250px",
              padding: "20px",
              background: "#FFC107",
              color: "black",
              borderRadius: "10px",
              margin: "10px",
              cursor: "pointer",
            }}
            onClick={() => navigate("/college-events")}
          >
            <h2>College Events</h2>
            <p>Participate in college activities.</p>
          </div>
          <div
            style={{
              width: "250px",
              padding: "20px",
              background: "#FF5733",
              color: "white",
              borderRadius: "10px",
              margin: "10px",
              cursor: "pointer",
            }}
            onClick={() => navigate("/club-events")}
          >
            <h2>Club Events</h2>
            <p>Join and participate in various club events.</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App; 