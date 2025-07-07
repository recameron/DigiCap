import React, { useState } from 'react';

export default function CreateCapsule() {
  const [formData, setFormData] = useState({
    message: '',
    recipientEmail: '',
    unlockDate: '',
  });

  const [errors, setErrors] = useState({});

  function validate() {
    const newErrors = {};

    if (!formData.message.trim()) {
      newErrors.message = 'Message is required.';
    } else if (formData.message.trim().length < 10) {
      newErrors.message = 'Message must be at least 10 characters.';
    }

    if (!formData.recipientEmail.trim()) {
      newErrors.recipientEmail = 'Recipient email is required.';
    } else if (
      !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(formData.recipientEmail)
    ) {
      newErrors.recipientEmail = 'Invalid email address.';
    }

    if (!formData.unlockDate) {
      newErrors.unlockDate = 'Unlock date is required.';
    } else {
      const today = new Date();
      const unlock = new Date(formData.unlockDate);
      if (unlock <= today) {
        newErrors.unlockDate = 'Unlock date must be in the future.';
      }
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  }

  function handleChange(e) {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    // Clear error on change
    setErrors(prev => ({ ...prev, [name]: null }));
  }

  function handleSubmit(e) {
  e.preventDefault();

  if (validate()) {
    console.log('Valid form submitted:', formData);

    // Build your payload — adjust field names to match your backend
    const payload = {
      message: formData.message,
      recipientEmail: formData.recipientEmail,
      unlockDate: formData.unlockDate
    };

    // Send POST request
    fetch("http://localhost:5000/api/entries", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to create capsule");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Success:", data);
        alert("Capsule created!");

        // Reset form
        setFormData({ message: "", recipientEmail: "", unlockDate: "" });
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("Something went wrong!");
      });
  }
}


  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-4 border rounded shadow">
      <h2 className="text-xl font-semibold mb-4">Create a Time Capsule</h2>

      <label className="block mb-2">
        Message:
        <textarea
          name="message"
          value={formData.message}
          onChange={handleChange}
          className={`w-full p-2 border rounded ${errors.message ? 'border-red-500' : ''}`}
          rows="4"
          required
        />
        {errors.message && <p className="text-red-600 text-sm mt-1">{errors.message}</p>}
      </label>

      <label className="block mb-2">
        Recipient Email:
        <input
          type="email"
          name="recipientEmail"
          value={formData.recipientEmail}
          onChange={handleChange}
          className={`w-full p-2 border rounded ${errors.recipientEmail ? 'border-red-500' : ''}`}
          required
        />
        {errors.recipientEmail && (
          <p className="text-red-600 text-sm mt-1">{errors.recipientEmail}</p>
        )}
      </label>

      <label className="block mb-4">
        Unlock Date:
        <input
          type="date"
          name="unlockDate"
          value={formData.unlockDate}
          onChange={handleChange}
          className={`w-full p-2 border rounded ${errors.unlockDate ? 'border-red-500' : ''}`}
          required
        />
        {errors.unlockDate && (
          <p className="text-red-600 text-sm mt-1">{errors.unlockDate}</p>
        )}
      </label>

      <button
        type="submit"
        className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 transition"
      >
        Create Capsule
      </button>
    </form>
  );
}
