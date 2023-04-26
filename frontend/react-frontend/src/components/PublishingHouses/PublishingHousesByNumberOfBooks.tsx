import {
  TableContainer,
  Paper,
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  CircularProgress,
  Container,
  IconButton,
  Tooltip,
} from "@mui/material";

import React from "react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

//import { BACKEND_API_URL } from "../../constants";
import { PublishingHouse } from "../../models/PublishingHouse";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";

export const PublishingHousesByNumberOfBooks = () => {
  const [loading, setLoading] = useState(false);
  const [publishingHouses, setPublishingHouses] = useState<PublishingHouse[]>(
    []
  );

  useEffect(() => {
    setLoading(true);
    fetch("http://127.0.0.1:8000/api/publishing-houses/count-smth/")
      .then((response) => response.json())
      .then((data) => {
        setPublishingHouses(data);

        setLoading(false);
      });
  }, []);

  return (
    <Container>
      <h1>sorted Publishing Houses</h1>

      {loading && <CircularProgress />}
      {!loading && publishingHouses.length === 0 && (
        <p>No publishing houses found</p>
      )}
      {!loading}

      {!loading && publishingHouses.length > 0 && (
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>#</TableCell>
                <TableCell align="right">Name</TableCell>
                <TableCell align="right">Headquarters</TableCell>
                <TableCell align="right">Founding Year</TableCell>
                <TableCell align="center">Books</TableCell>
              </TableRow>
            </TableHead>

            <TableBody>
              {publishingHouses.map((publishingHouse, index) => (
                <TableRow key={publishingHouse.id}>
                  <TableCell component="th" scope="row">
                    {index + 1}
                  </TableCell>

                  <TableCell component="th" scope="row">
                    <Link
                      to={`/publishing-house/${publishingHouse.id}/details`}
                      title="View publishing house details"
                    >
                      {publishingHouse.name}
                    </Link>
                  </TableCell>

                  <TableCell align="right">
                    {publishingHouse.headquarters}
                  </TableCell>
                  <TableCell align="right">
                    {publishingHouse.founding_year}
                  </TableCell>
                  {publishingHouse["books"]?.length}
                  <TableCell align="right"></TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Container>
  );
};
