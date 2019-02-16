import React, { Component } from "react";
import "./WelcomePage.css";
import axios from "axios";

class WelcomePage extends Component {
  constructor(props) {
    super(props);
    this.state = { step: "login" };
  }

  handleStepChange = step_name => {
    this.setState({ step: step_name });
  };

  content = step_name => {
    if (this.state.step === "signup") {
      return <Signup handleStepChange={this.handleStepChange} saveToken={this.props.saveToken} />;
    } else if (this.state.step === "main_menu") {
      return (
        <MainMenu
          handleStepChange={this.handleStepChange}
          handlePageChange={this.props.handlePageChange}
          token={this.props.token}
        />
      );
    } else if (this.state.step === "create_game") {
      return (
        <Creategame
          handleStepChange={this.handleStepChange}
          handlePageChange={this.props.handlePageChange}
          token={this.props.token}
        />
      );
    } else {
      return <Login handleStepChange={this.handleStepChange} saveToken={this.props.saveToken} />; //par défaut, la page est sur login, à revoir
    }
  };
  render() {
    return <div className="welcome-grid">{this.content(this.state.step)}</div>;
  }
}

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "Username",
      password: "Password"
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
    axios.post('http://127.0.0.1:8000/api/v1/users/login/', {
      "user": {
        "username": this.state.username,
        "password": this.state.password
      }
    })
      .then(response => {
        let report = '';
        for (let key in response.data.user) {
          report += "\n" + key + ' : ' + response.data.user[key];
        };
        console.log(report);
        this.props.handleStepChange('main_menu');
        this.props.saveToken(response.data.user.token);
      })
      .catch(error => {
        let report = '';
        for (let key in error.response.data.errors) {
          report += "\n" + key + ' : ' + error.response.data.errors[key];
        }
        console.log(report);
      });
    event.preventDefault();
  }

  render() {
    return (
      <div className="menu-box">
        <form onSubmit={this.handleSubmit}>
          <label>
            <input
              name="username"
              value={this.state.username}
              onChange={this.handleChange}
              placeholder="Username"
            />
          </label>
          <br />
          <label>
            <input
              name="password"
              type="password"
              value={this.state.password}
              onChange={this.handleChange}
              placeholder="Password"
            />
          </label>
          <br />
          <input type="submit" value="Login" />
        </form>
        <div
          className="hover"
          onClick={() => this.props.handleStepChange("signup")}
        >
          {" "}
          No account yet? Create one!{" "}
        </div>
      </div>
    );
  }
}

class Signup extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      email: "",
      password: "",
      passwordCheck: "",
      check: false
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
    this.setState({
      check:
        this.state.password === this.state.passwordCheck &&
        this.validateEmail(this.state.email)
    });
  }

  handleSubmit(event) {
    if (true || this.state.check) { // !!!!!!!!!!!!!!!!!!!!!!!
      axios.post('http://127.0.0.1:8000/api/v1/users/', {
        "user": {
          "username": this.state.username,
          "email": this.state.email,
          "password": this.state.password
        }
      })
        .then(response => {
          let report = '';
          for (let key in response.data.user) {
            report += "\n" + key + ' : ' + response.data.user[key];
          }
          console.log(report);
          this.props.handleStepChange('main_menu');
          this.props.saveToken(response.data.user.token);
        })
        .catch(error => {
          let report = '';
          for (let key in error.response.data.errors) {
            report += "\n" + key + ' : ' + error.response.data.errors[key];
          }
          console.log(report);
        });
    } else alert("Something isn't right !");
    event.preventDefault();
  }

  validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
  }

  render() {
    return (
      <div className="menu-box">
        <form onSubmit={this.handleSubmit}>
          <label>
            <input
              name="username"
              value={this.state.username}
              onChange={this.handleChange}
              placeholder="Username"
            />
          </label>
          <br />
          <label>
            <input
              name="email"
              value={this.state.email}
              onChange={this.handleChange}
              placeholder="Email address"
            />
          </label>
          <br />
          <label>
            <input
              name="password"
              type="password"
              value={this.state.password}
              onChange={this.handleChange}
              placeholder="Password"
            />
          </label>
          <br />
          <label>
            <input
              name="passwordCheck"
              type="password"
              value={this.state.passwordCheck}
              onChange={this.handleChange}
              placeholder="Check your password"
            />
          </label>
          <br />
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}

class MainMenu extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div className="main-menu">
        <JoinGame
          handlePageChange={this.props.handlePageChange}
          handleStepChange={this.handleStepChange}
          token={this.props.token}
        />
        <Button
          text="Create new game"
          onClick={() => this.props.handleStepChange("create_game")}
        />
      </div>
    );
  }
}

class Button extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div className="main-menu-button hover" onClick={this.props.onClick}>
        {this.props.text}
      </div>
    );
  }
}

class Creategame extends Component {
  constructor(props) {
    super(props);
    this.state = {
      game_was_created: false,
      join_token: null
    };
  }
  handleGameCreation = () => {
    axios.post('http://127.0.0.1:8000/api/v1/games/', {
      "game": { "version": "jelly" }
    }, { headers: { "Authorization": "Token " + this.props.token } })
      .then(response => {
        this.setState({
          game_was_created: true,
          join_token: response.data.game.join_token
        })
        let report = '';
        for (let key in response.data.game) {
          report += "\n" + key + ' : ' + response.data.game[key];
        }
        console.log(report);
      })
      .catch(error => {
        let report = '';
        for (let key in error.response.data.errors) {
          report += "\n" + key + ' : ' + error.response.data.errors[key];
        }
        console.log(report);
      });
  };
  render() {
    if (this.state.game_was_created) {
      return (
        <div className="menu-box">
          <BackButton
            onClick={() => this.props.handleStepChange("main_menu")}
          />
          <p> Your Join Token is: </p>
          <p> {this.state.join_token} </p>
          <p>
            {" "}
            You may copy it and share it with the people you want to join the
            game.
          </p>
          <Button
            text="Start the game"
            onClick={() => this.props.handlePageChange()}
          />
        </div>
      );
    } else {
      return (
        <div className="create-game">
          <BackButton
            onClick={() => this.props.handleStepChange("main_menu")}
          />
          <p>
            {" "}
            If you click on "create new game", you will get a game code that you
            will have to send to your friends. They must have it to join your
            game.
          </p>
          <Button text="Create a new game" onClick={this.handleGameCreation} />
        </div>
      );
    }
  }
}

class JoinGame extends Component {
  constructor(props) {
    super(props);
    this.state = { join_token: "" };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  };
  handleSubmit(event) {
    axios.post('http://127.0.0.1:8000/api/v1/players/', {
      "player": {
        "join_token": this.state.join_token
      }
    }, { headers: { "Authorization": "Token " + this.props.token } })
      .then(response => {
        let report = '';
        for (let key in response.data.player) {
          report += "\n" + key + ' : ' + response.data.player[key];
        }
        console.log(report);
        this.props.handlePageChange();
      })
      .catch(error => {
        let report = '';
        for (let key in error.response.data.errors) {
          report += "\n" + key + ' : ' + error.response.data.errors[key];
        }
        console.log(report);
      });
    event.preventDefault();
  };
  render() {
    return (
      <div className="menu-box">
        <form onSubmit={this.handleSubmit}>
          <label>
            Join Token:
            <input
              name="join_token"
              value={this.state.join_token}
              onChange={this.handleChange}
              placeholder="Paste your Join Token here !"
            />
          </label>
          <input type="submit" value="Join" />
        </form>
      </div>
    );
  }
}

class BackButton extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div className="back-button hover" onClick={this.props.onClick}>
        Back
      </div>
    );
  }
}

export default WelcomePage;
