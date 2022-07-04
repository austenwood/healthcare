import React from "react";
import { Button, ButtonGroup } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

function Landing() {
  return (
    <div className="middle-center">
      <h1 className="landing logo">Healthcare</h1>
      {
        <ButtonGroup>
          <LinkContainer to="/search">
            <Button>Search</Button>
          </LinkContainer>
          <LinkContainer to="/upload">
            <Button>Upload</Button>
          </LinkContainer>
        </ButtonGroup>
      }
    </div>
  );
}

export default Landing;
