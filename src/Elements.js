import React, { Component } from "react";
import "./App.css";

class MainGrid extends Component {
  state = {
    current_tab: "Menu",
    current_action_queue: [
      <ActionIcon className="action-icon img-building" />,
      <ActionIcon className="action-icon img-building" />,
      <ActionIcon className="action-icon img-building" />,
      <ActionIcon className="action-icon img-building" />,
      <ActionIcon className="action-icon img-building" />,
      <ActionIcon className="action-icon img-building" />
    ]
  };
  handleTabChange = tab_name => {
    let new_state = this.state;
    new_state.current_tab = tab_name;
    this.setState(new_state);
  };
  handleActionQueue = (action_name, delete_action = false) => {
    if (delete_action) {
      if (this.state.current_action_queue.length > 0) {
        let new_state = this.state;
        new_state.current_action_queue.pop();
        this.setState(new_state);
      }
    } else {
      let new_state = this.state;
      new_state.current_action_queue.push(
        <ActionIcon className={"action-icon " + action_name} />
      ); // à modifier!!!!!!!!!!!!!!
      console.log("action-icon " + action_name);
      this.setState(new_state);
    }
  };
  getMainState = () => {
    return this.state;
  };
  render() {
    if (this.state.current_tab == "Technologies")
      return (
        <div className="main-grid">
          <MainHeader handleTabChange={this.handleTabChange} />
          <TechGrid />
        </div>
      );
    else
      return (
        <div className="main-grid">
          <MainHeader handleTabChange={this.handleTabChange} />
          <MenuGrid
            getMainState={this.getMainState}
            handleActionQueue={this.handleActionQueue}
          />
        </div>
      );
  }
}

class MainHeader extends Component {
  render() {
    return (
      <div className="main-header">
        <Tab text="Menu" handleTabChange={this.props.handleTabChange} />
        <Tab text="Technologies" handleTabChange={this.props.handleTabChange} />
      </div>
    );
  }
}

class Tab extends Component {
  render() {
    return (
      <div
        className="tab hover"
        onClick={() => this.props.handleTabChange(this.props.text)}
      >
        {this.props.text}
      </div>
    );
  }
}

class MenuGrid extends Component {
  render() {
    return (
      <div className="menu-grid">
        <MenuDisplay />
        <MenuMonitor />
        <MenuActionQueue
          getMainState={this.props.getMainState}
          handleActionQueue={this.props.handleActionQueue}
        />
        <MenuFooter handleActionQueue={this.props.handleActionQueue} />
      </div>
    );
  }
}

class MenuDisplay extends Component {
  render() {
    return <div className="menu-display hover">DISPLAY</div>;
  }
}

class MenuMonitor extends Component {
  render() {
    return (
      <div className="menu-monitor">
        <MenuMonitorStats text="STATS 1" />
        <MenuMonitorStats text="STATS 2" />
        <MenuMonitorStats text="STATS 3" />
        <MenuMonitorStats text="STATS 4" />
      </div>
    );
  }
}

class MenuMonitorStats extends Component {
  render() {
    return <div className="menu-monitor-stats hover">{this.props.text}</div>;
  }
}

class MenuFooter extends Component {
  state = { current_info: undefined };
  handleInformation = info => {
    this.setState({ current_info: info });
  };
  render() {
    return (
      <div className="menu-footer">
        <MenuFooterTabs />
        <MenuFooterActions
          handleInformation={this.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <MenuFooterInformationPannel
          info={this.state.current_info}
          handleActionQueue={this.props.handleActionQueue}
        />
      </div>
    );
  }
}

class MenuFooterTabs extends Component {
  render() {
    return (
      <div className="menu-footer-tabs">
        <BoxHover text="TAB 1" />
        <BoxHover text="TAB 2" />
        <BoxHover text="TAB 3" />
      </div>
    );
  }
}
class MenuFooterActions extends Component {
  render() {
    let actionsWidth = ((window.innerWidth / 10.3) * 0.8 * 2) / 3;
    let actionsGap = ((window.innerWidth / 11) * 0.2 * 2) / 3;
    let style = {
      display: "grid",
      gridTemplateColumns: "repeat(10, " + actionsWidth + "px)",
      gridAutoFlow: "row",
      gridAutoRows: actionsWidth,
      gridRow: "2",
      gridColumn: "1",
      gridGap: actionsGap,
      paddingTop: "1em",
      paddingBottom: "1em",
      paddingLeft: "1em",
      paddingRight: "1em",
      border: "0.01em solid #fff435",
      height: "7em",
      overflowY: "auto"
    };

    return (
      <div style={style}>
        <Action
          name="img-building"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-chimneys"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-factory"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-building"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-chimneys"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-factory"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-building"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-chimneys"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-factory"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-building"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-chimneys"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-factory"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-building"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-chimneys"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
        <Action
          name="img-factory"
          handleInformation={this.props.handleInformation}
          handleActionQueue={this.props.handleActionQueue}
        />
      </div>
    );
  }
}

class Action extends Component {
  state = { info: this.props.name }; //temporary (while no real info to display)
  render() {
    return (
      <div
        className={"action " + this.props.name}
        onMouseOver={() => this.props.handleInformation(this.state.info)}
        onMouseOut={() => this.props.handleInformation(undefined)}
        onClick={() => this.props.handleActionQueue(this.props.name)}
      />
    );
  }
}

class MenuFooterInformationPannel extends Component {
  render() {
    if (this.props.info) {
      return (
        <div className="menu-footer-information-pannel">{this.props.info}</div>
      );
    } //in case it is undefined
    else {
      return (
        <div className="menu-footer-information-pannel hover">
          <p> </p>
          <p onClick={() => this.props.handleActionQueue("", true)}>
            Undo last action
          </p>
          <p> </p>
        </div>
      );
    }
  }
}

class BoxHover extends Component {
  render() {
    return <div className="box hover">{this.props.text}</div>;
  }
}

class MenuActionQueue extends Component {
  render() {
    return (
      <div className="menu-action-queue">
        {this.props.getMainState().current_action_queue.map(a => a)}
      </div>
    );
  }
}

class ActionIcon extends Component {
  render() {
    return <div className={this.props.className} />;
  }
}

//Components from technology tab

class TechGrid extends Component {
  render() {
    return (
      <div className="tech-grid">
        <TechTree />
      </div>
    );
  }
}

class TechTree extends Component {
  render() {
    return (
      <div className="tech-tree">
        <BoxHover text="TAB 1" />
        <BoxHover text="TAB 2" />
        <BoxHover text="TAB 3" />
        <BoxHover text="TAB 1" />
        <BoxHover text="TAB 2" />
        <BoxHover text="TAB 3" />
        <BoxHover text="TAB 1" />
        <BoxHover text="TAB 2" />
        <BoxHover text="TAB 3" />
        <BoxHover text="TAB 1" />
        <BoxHover text="TAB 2" />
        <BoxHover text="TAB 3" />
        <BoxHover text="TAB 1" />
        <BoxHover text="TAB 2" />
        <BoxHover text="TAB 3" />
      </div>
    );
  }
}

export default MainGrid;
