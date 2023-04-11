import { useEffect, useState } from "react";
import { PublishingHouse } from "../../models/PublishingHouse";

export const PublishingHouseShowAll = () => {
  const [publishingHouses, setPubllishingHouses] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/publishing-house/")
      .then((res) => res.json())
      .then((data) => setPubllishingHouses(data));
  }, []); // when to rerendeer the page kinda

  return (
    <div className="App">
      <h1>Publishing House List</h1>
      <table>
        <tr>
          <th>#</th>
          <th>Publishing house name </th>
          <th>Headquarters</th>
          <th>Founding year</th>
        </tr>
        {publishingHouses.map((publishingHouse: PublishingHouse, index) => (
          <tr key={index}>
            <td>(index) </td>
            <td>(publishingHouse.name) </td>
            <td>(publishingHouse.headquarters) </td>
            <td>(publishingHouse.founding_year) </td>
          </tr>
        ))}
      </table>
    </div>
  );
};
