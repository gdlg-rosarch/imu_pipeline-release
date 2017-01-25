Name:           ros-indigo-imu-pipeline
Version:        0.2.2
Release:        0%{?dist}
Summary:        ROS imu_pipeline package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/imu_pipeline
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-imu-processors
Requires:       ros-indigo-imu-transformer
BuildRequires:  ros-indigo-catkin

%description
imu_pipeline

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jan 25 2017 Paul Bovbel <pbovbel@clearpathrobotics.com> - 0.2.2-0
- Autogenerated by Bloom

* Wed Feb 04 2015 Paul Bovbel <pbovbel@clearpathrobotics.com> - 0.2.1-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Paul Bovbel <pbovbel@clearpathrobotics.com> - 0.2.0-0
- Autogenerated by Bloom

