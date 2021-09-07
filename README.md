# amr_interop_bridge

This is client for communication according to the MassRobotics AMR Interoperability Standard.
it sends ROS1 topics to the AMR Interoperability Receiver via websockets. ( Receiving is not supported. )

## How to move it
Since it contains nodes that simulate ROS1 topics, you can try to run it immediately.

### 1. install the MassRobotics AMR Interoperability Standard Receiver

Please refer to the link.
https://github.com/MassRobotics-AMR/AMR_Interop_Standard

### 2. Clone the repository to catkin_workspace under src

example
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
$ cd src
$ git clone git@github.com:LexxPluss/amr_interop_bridge.git
```

### 3. Clear dependencies

example
```
$ pip2 install websocket-client pytz
```

### 4. Build and load

example
```
$ cd ~/catkin_ws/
$ catkin_make
$ source devel/setup.bash
```

### 5. Execute

#### example1 : send minimum required
```
$ roslaunch amr_interop_bridge amr_interop_bridge_required.launch
```

#### example2 : send minimum required ( specify the server. by default, connect to ws://localhost:3000 )
```
$ roslaunch amr_interop_bridge amr_interop_bridge_required.launch url:=ws://SERVER-ADDRESS
```

#### example3 : send full properties
```
$ roslaunch amr_interop_bridge amr_interop_bridge_full.launch
```
