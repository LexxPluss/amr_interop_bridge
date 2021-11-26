cmake_minimum_required(VERSION 3.0.2)
project(amr_interop_bridge)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  amr_interop_msgs
)

catkin_package(
  CATKIN_DEPENDS
  rospy
  std_msgs
  geometry_msgs
  amr_interop_msgs
)

catkin_install_python(PROGRAMS
  scripts/fake_base_robot_envelope.py
  scripts/fake_battery_percentage.py
  scripts/fake_cargo_max_volume.py
  scripts/fake_charger_type.py
  scripts/fake_cargo_max_weight.py
  scripts/fake_cargo_type.py
  scripts/fake_emergency_contact_information.py
  scripts/fake_error_codes.py
  scripts/fake_load_percentage_still_avaiable.py
  scripts/fake_location.py
  scripts/fake_manufacture_name.py
  scripts/fake_max_run_time.py
  scripts/fake_max_speed.py
  scripts/fake_operational_state.py
  scripts/fake_path_and_destinations.py
  scripts/fake_product_documentation.py
  scripts/fake_remaining_run_time.py
  scripts/fake_robot_model.py
  scripts/fake_robot_serial_number.py
  scripts/fake_support_vendor_contact_information.py
  scripts/fake_support_vendor_name.py
  scripts/fake_thumbnail_image.py
  scripts/fake_uuid.py
  scripts/fake_velocity.py
  scripts/amr_interop_bridge.py

  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
