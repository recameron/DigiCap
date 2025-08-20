import React from "react";

export default function Header() {
  return (
    <header className="flex items-center p-4 bg-white shadow-md">
      <img
        src="https://storage.googleapis.com/digicap-components/Images/digicap_logo-removebg-preview.png"
        alt="DigiCap Logo"
        className="h-16 w-auto mr-3"
      />
      <h1 className="text-xl font-bold text-indigo-700"></h1>
    </header>
  );
}