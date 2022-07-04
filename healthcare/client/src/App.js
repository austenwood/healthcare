import { Container, Navbar } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";
import { Outlet, Route, Routes } from "react-router-dom";

import Landing from "./components/Landing.js";
import Upload from "./components/Upload";
import Search from "./components/Search";

import "./App.css";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Landing />} />
        <Route path="search" element={<Search />} />
        <Route path="upload" element={<Upload />} />
      </Route>
    </Routes>
  );
}

function Layout() {
  return (
    <>
      <Navbar bg="light" expand="lg" variant="light">
        <Container>
          <LinkContainer to="/">
            <Navbar.Brand className="logo">Healthcare</Navbar.Brand>
          </LinkContainer>
        </Container>
      </Navbar>
      <Container className="pt-3">
        <Outlet />
      </Container>
    </>
  );
}

export default App;
