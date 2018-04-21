# Script generated with Bloom
pkgdesc="ROS - Node/nodelet combination to transform sensor_msgs::Imu data from one frame into another."
url='http://ros.org/wiki/imu_transformer'

pkgname='ros-kinetic-imu-transformer'
pkgver='0.2.2_1'
pkgrel=1
arch=('any')
license=('GPL'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-roscpp'
'ros-kinetic-roslaunch'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf2'
'ros-kinetic-tf2-ros'
'ros-kinetic-tf2-sensor-msgs'
'ros-kinetic-topic-tools'
)

depends=('ros-kinetic-geometry-msgs'
'ros-kinetic-message-filters'
'ros-kinetic-nodelet'
'ros-kinetic-roscpp'
'ros-kinetic-roslaunch'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf2'
'ros-kinetic-tf2-ros'
'ros-kinetic-tf2-sensor-msgs'
'ros-kinetic-topic-tools'
)

conflicts=()
replaces=()

_dir=imu_transformer
source=()
md5sums=()

prepare() {
    cp -R $startdir/imu_transformer $srcdir/imu_transformer
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

