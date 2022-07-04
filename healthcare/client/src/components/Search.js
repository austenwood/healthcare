import React, { useState} from "react";
import axios from "axios";
import { Formik } from "formik";
import { Button, Card, Form, Table } from "react-bootstrap";

function Search() {
  const [data, setData] = useState(null);
  const [isSubmitted, setSubmitted] = useState(false);

  const onSubmit = async (values) => {
    const url = "http://localhost:8000/api/members/";
    const formData = new FormData();

    formData.append("id", values.id);
    formData.append("account_id", values.accountId);
    formData.append("phoneNumber", values.phoneNumber);
    formData.append("clientMemberId", values.clientMemberId);

    try {
      const response = await axios.get(url, {
        params: {
          id: values.id,
          account_id: values.accountId,
          phone_number: values.phoneNumber,
          client_member_id: values.clientMemberId,
        },
      });
      setData(response.data);
      setSubmitted(true);
    } catch (err) {
      console.log(err);
    }
  };

  const sayHello = () => {
    setSubmitted(false);
  };

  if (isSubmitted) {
    return (
      <>
        <Card className="mb-3">
          <Card.Header>Results</Card.Header>
          <Card.Body>
            <div className="d-grid mb-3">
              <Button onClick={sayHello} type="submit" variant="primary">
                New Search
              </Button>
            </div>
            <Table striped bordered hover size="sm">
              <thead>
                <tr>
                  <th>First Name</th>
                  <th>Last Name</th>
                  <th>Account ID</th>
                  <th>Phone Number</th>
                  <th>Client Member ID</th>
                </tr>
              </thead>
              <tbody>
                {data.map((member) => (
                  <tr>
                    <td>{member.first_name}</td>
                    <td>{member.last_name}</td>
                    <td>{member.account_id}</td>
                    <td>{member.phone_number}</td>
                    <td>{member.client_member_id}</td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </Card.Body>
        </Card>
      </>
    );
  }

  return (
    <>
      <Card className="mb-3">
        <Card.Header>Search</Card.Header>
        <Card.Body>
          <Formik
            initialValues={{
              id: "",
              accountId: "",
              phoneNumber: "",
              clientMemberId: "",
            }}
            onSubmit={onSubmit}
          >
            {({ handleChange, handleSubmit, values }) => (
              <Form noValidate onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="id">
                  <Form.Label>ID:</Form.Label>
                  <Form.Control
                    name="id"
                    onChange={handleChange}
                    values={values.id}
                  />
                </Form.Group>
                <Form.Group className="mb-3" controlId="accountId">
                  <Form.Label>Account ID:</Form.Label>
                  <Form.Control
                    name="accountId"
                    onChange={handleChange}
                    values={values.accountId}
                  />
                </Form.Group>
                <Form.Group className="mb-3" controlId="phoneNumber">
                  <Form.Label>Phone Number:</Form.Label>
                  <Form.Control
                    name="phoneNumber"
                    onChange={handleChange}
                    values={values.phoneNumber}
                  />
                </Form.Group>
                <Form.Group className="mb-3" controlId="clientMemberId">
                  <Form.Label>Client Member ID:</Form.Label>
                  <Form.Control
                    name="clientMemberId"
                    onChange={handleChange}
                    type=""
                    value={values.clientMemberId}
                  />
                </Form.Group>
                <div className="d-grid">
                  <Button type="submit" variant="primary">
                    Submit
                  </Button>
                </div>
              </Form>
            )}
          </Formik>
        </Card.Body>
      </Card>
    </>
  );
}

export default Search;
