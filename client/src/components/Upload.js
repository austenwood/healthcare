import React, { useState } from "react";
import axios from "axios";
import { Formik } from "formik";
import { Button, Card, Form } from "react-bootstrap";
import { Navigate } from "react-router-dom";

function Upload() {
  const [isSubmitted, setSubmitted] = useState(false);

  const onSubmit = async (values) => {
    const url = "http://localhost:8000/api/upload/";
    const formData = new FormData();

    formData.append("file", values.file);

    const response = await axios.post(url, formData);
    setSubmitted(true);
    console.log(response);
  };

  if (isSubmitted) {
    return <Navigate to="/#" />;
  }

  return (
    <>
      <Card className="mb-3">
        <Card.Header>Upload</Card.Header>
        <Card.Body>
          <Formik
            initialValues={{
              file: [],
            }}
            onSubmit={onSubmit}
          >
            {({ handleSubmit, isSubmitting, setFieldValue }) => (
              <Form noValidate onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="file">
                  <Form.Label>File:</Form.Label>
                  <Form.Control
                    name="file"
                    onChange={(event) => {
                      setFieldValue("file", event.currentTarget.files[0]);
                    }}
                    required
                    type="file"
                  />
                </Form.Group>
                <div className="d-grid">
                  <Button
                    disabled={isSubmitting}
                    type="submit"
                    variant="primary"
                  >
                    Upload
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

export default Upload;
