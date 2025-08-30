import Image from "next/image";
import "../styles/landing.css";
export default function Home() {
  return (
    <div className="wrapper">
      <div id="form-container">
      <p className="logo">
        Ripple
      </p>
      <form autoComplete="off" className="form">
        <input type="text" placeholder="Username" />
        <div className="inner-form">
          <input type="password" placeholder="Password" />
          <button type="submit">Login</button>
        </div>
      </form>

      </div>
    </div>
  );
}
