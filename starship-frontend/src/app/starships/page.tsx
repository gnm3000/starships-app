"use client";
import { useEffect, useState } from 'react';
import { useAuth } from '../../context/AuthContext';
import axios from 'axios';
import { useRouter } from 'next/navigation';

interface Starship {
  name: string;
  model: string;
  manufacturer: string;
}

const Starships = () => {
  const { token, isLoading } = useAuth();
  const router = useRouter();
  const [manufacturers, setManufacturers] = useState<string[]>([]);
  const [selectedManufacturer, setSelectedManufacturer] = useState<string>('');
  const [starships, setStarships] = useState<Starship[]>([]);

  useEffect(() => {
    if (!isLoading) {
      // isLoading allows that dont redirect faster than we want
      // is loading is false, when we already have the token from localstorage
      if (!token) {
        router.push('/login');
      } else {
        // let's pass the jwt token we got to the functions to make the api call
        fetchManufacturers(token);
        fetchStarships(token, '');
      }
    }
  }, [token, isLoading]);

  useEffect(() => {
    if (token && !isLoading) {
      if (selectedManufacturer) {
        // case select specific manufacturer
        fetchStarships(token, selectedManufacturer);
      } else {
        // if we need to show all the records
        fetchStarships(token, '');
      }
    }
  }, [selectedManufacturer, token, isLoading]);

  const fetchManufacturers = async (token: string) => {
    try {
      const response = await axios.get('http://localhost:5000/bff/manufacturers', {
        headers: { Authorization: `Bearer ${token}` },
      });
      // getting data from API manufacturers
      setManufacturers(response.data.manufacturers);
    } catch (error) {
      console.error('Error setManufacturers:', error);
    }
  };

  const fetchStarships = async (token: string, manufacturer: string = '') => {
    try {
      // here we have the case when we want from specific manufacturer or not.
      // and we need to send the token that we get from context
      const url = manufacturer
        ? `http://localhost:5000/bff/starships?manufacturer=${manufacturer}`
        : 'http://localhost:5000/bff/starships';
      const response = await axios.get(url, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setStarships(response.data.starships); 
    } catch (error) {
      console.error('Error fetchStarships:', error);
    }
  };
  // meanwhile we wait for get token from localStorage
  if (isLoading) return <div>Loading...</div>;

  return (
    <div>
      <h1>Starships</h1>
      <select
        value={selectedManufacturer}
        onChange={(e) => setSelectedManufacturer(e.target.value)}
      >
        <option value="">All Manufacturers</option>
        {manufacturers.map((manufacturer) => (
          <option key={manufacturer} value={manufacturer}>
            {manufacturer}
          </option>
        ))}
      </select>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Model</th>
            <th>Manufacturer</th>
          </tr>
        </thead>
        <tbody>
          {starships.map((starship) => (
            <tr key={starship.name}>
              <td>{starship.name}</td>
              <td>{starship.model}</td>
              <td>{starship.manufacturer}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Starships;
