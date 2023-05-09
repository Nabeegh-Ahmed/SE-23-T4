import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./Header.css";

export const Header = () => {
  const [open, setopen] = useState(false);
  console.log(open);
  return (
    <>
      <div className="headermain">
        <div className="header">
          <div className="left">
            <img
              src="https://nftify-platform.s3.ap-southeast-1.amazonaws.com/logo/62d170f22994a0bed7213b80-1658926016888.png"
              alt=""
            />
            <form
              classname="example"
              action="/action_page.php"
              style={{ margin: "auto", maxWidth: "300px" }}
            >
              <input type="text" placeholder="Search.." name="search2" />
            </form>
          </div>
          <div className="right">
            <div className="nav">
              <span>Home</span>
              <span>Discover</span>
              <span>Activity</span>
              <Link to="/">
                {" "}
                <span> AI Bot </span>{" "}
              </Link>
              <span>
                <Link to="/ImageGenator"> Image Generator </Link>
              </span>
            </div>
          </div>
          <img
            className="HeaderHamburger"
            src="https://www.lbac.app/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhamburger.bd56af02.png&w=96&q=75"
            onClick={() => {
              setopen((open) => !open);
            }}
          />
        </div>
      </div>
      <div className={!open ? "links" : "links l-f-m"}>
        <div className="nav-f-m">
          <div>Home</div>
          <div>Discover</div>
          <div>Activity</div>
          <div>
            <Link to="/"> AI Bot </Link>
          </div>
          <div>
            <Link to="/ImageGenator"> Image Generator </Link>
          </div>
        </div>
      </div>
    </>
  );
};
