#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFE0B6D736B1195ED (akulichalexander@gmail.com)
#
Name     : telepathy-qt
Version  : 0.9.7
Release  : 13
URL      : https://telepathy.freedesktop.org/releases/telepathy-qt/telepathy-qt-0.9.7.tar.gz
Source0  : https://telepathy.freedesktop.org/releases/telepathy-qt/telepathy-qt-0.9.7.tar.gz
Source1  : https://telepathy.freedesktop.org/releases/telepathy-qt/telepathy-qt-0.9.7.tar.gz.asc
Summary  : Qt Telepathy Service side bindings
Group    : Development/Tools
License  : LGPL-2.1
Requires: telepathy-qt-lib = %{version}-%{release}
Requires: telepathy-qt-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : dbus-dev
BuildRequires : dbus-glib-dev
BuildRequires : doxygen
BuildRequires : extra-cmake-modules pkgconfig(glib-2.0)
BuildRequires : farstream-dev
BuildRequires : libxml2-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(farstream-0.2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(telepathy-glib)
BuildRequires : python-core
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : qtbase-dev
Patch1: py2.patch
Patch2: 0001-Fix-wrong-version-number-matching.patch

%description
=============
telepathy-qt
=============
This is a library for Qt-based Telepathy clients.

%package dev
Summary: dev components for the telepathy-qt package.
Group: Development
Requires: telepathy-qt-lib = %{version}-%{release}
Provides: telepathy-qt-devel = %{version}-%{release}
Requires: telepathy-qt = %{version}-%{release}

%description dev
dev components for the telepathy-qt package.


%package lib
Summary: lib components for the telepathy-qt package.
Group: Libraries
Requires: telepathy-qt-license = %{version}-%{release}

%description lib
lib components for the telepathy-qt package.


%package license
Summary: license components for the telepathy-qt package.
Group: Default

%description license
license components for the telepathy-qt package.


%prep
%setup -q -n telepathy-qt-0.9.7
cd %{_builddir}/telepathy-qt-0.9.7
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602608622
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DPYTHON_EXECUTABLE=/usr/bin/python2
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1602608622
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/telepathy-qt
cp %{_builddir}/telepathy-qt-0.9.7/COPYING %{buildroot}/usr/share/package-licenses/telepathy-qt/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr
mv %{buildroot}/builddir/build/BUILD/telepathy-qt-*/clr-build/* %{buildroot}/usr
for f in %{buildroot}/usr/lib64/cmake/TelepathyQt5/* ; do
sed -i 's|builddir/build/BUILD/telepathy-qt-.*/clr-build|usr|' $f
done
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/telepathy-qt5/TelepathyQt/AbstractAdaptor
/usr/include/telepathy-qt5/TelepathyQt/AbstractClient
/usr/include/telepathy-qt5/TelepathyQt/AbstractClientApprover
/usr/include/telepathy-qt5/TelepathyQt/AbstractClientHandler
/usr/include/telepathy-qt5/TelepathyQt/AbstractClientObserver
/usr/include/telepathy-qt5/TelepathyQt/AbstractDBusServiceInterface
/usr/include/telepathy-qt5/TelepathyQt/AbstractInterface
/usr/include/telepathy-qt5/TelepathyQt/AbstractProtocolInterface
/usr/include/telepathy-qt5/TelepathyQt/Account
/usr/include/telepathy-qt5/TelepathyQt/AccountCapabilityFilter
/usr/include/telepathy-qt5/TelepathyQt/AccountFactory
/usr/include/telepathy-qt5/TelepathyQt/AccountFilter
/usr/include/telepathy-qt5/TelepathyQt/AccountInterface
/usr/include/telepathy-qt5/TelepathyQt/AccountInterfaceAddressingInterface
/usr/include/telepathy-qt5/TelepathyQt/AccountInterfaceAvatarInterface
/usr/include/telepathy-qt5/TelepathyQt/AccountInterfaceStorageInterface
/usr/include/telepathy-qt5/TelepathyQt/AccountManager
/usr/include/telepathy-qt5/TelepathyQt/AccountManagerInterface
/usr/include/telepathy-qt5/TelepathyQt/AccountPropertyFilter
/usr/include/telepathy-qt5/TelepathyQt/AccountSet
/usr/include/telepathy-qt5/TelepathyQt/AndFilter
/usr/include/telepathy-qt5/TelepathyQt/AuthenticationTLSCertificateInterface
/usr/include/telepathy-qt5/TelepathyQt/AvatarData
/usr/include/telepathy-qt5/TelepathyQt/AvatarSpec
/usr/include/telepathy-qt5/TelepathyQt/BaseCall
/usr/include/telepathy-qt5/TelepathyQt/BaseChannel
/usr/include/telepathy-qt5/TelepathyQt/BaseConnection
/usr/include/telepathy-qt5/TelepathyQt/BaseConnectionManager
/usr/include/telepathy-qt5/TelepathyQt/BaseDebug
/usr/include/telepathy-qt5/TelepathyQt/BaseProtocol
/usr/include/telepathy-qt5/TelepathyQt/BaseProtocolAddressingInterface
/usr/include/telepathy-qt5/TelepathyQt/BaseProtocolAvatarsInterface
/usr/include/telepathy-qt5/TelepathyQt/BaseProtocolPresenceInterface
/usr/include/telepathy-qt5/TelepathyQt/CallChannel
/usr/include/telepathy-qt5/TelepathyQt/CallContent
/usr/include/telepathy-qt5/TelepathyQt/CallContentInterface
/usr/include/telepathy-qt5/TelepathyQt/CallContentInterfaceAudioControlInterface
/usr/include/telepathy-qt5/TelepathyQt/CallContentInterfaceDTMFInterface
/usr/include/telepathy-qt5/TelepathyQt/CallContentInterfaceMediaInterface
/usr/include/telepathy-qt5/TelepathyQt/CallContentInterfaceVideoControlInterface
/usr/include/telepathy-qt5/TelepathyQt/CallContentMediaDescription
/usr/include/telepathy-qt5/TelepathyQt/CallContentMediaDescriptionInterface
/usr/include/telepathy-qt5/TelepathyQt/CallContentMediaDescriptionInterfaceRTCPExtendedReportsInterface
/usr/include/telepathy-qt5/TelepathyQt/CallContentMediaDescriptionInterfaceRTCPFeedbackInterface
/usr/include/telepathy-qt5/TelepathyQt/CallContentMediaDescriptionInterfaceRTPHeaderExtensionsInterface
/usr/include/telepathy-qt5/TelepathyQt/CallStream
/usr/include/telepathy-qt5/TelepathyQt/CallStreamEndpoint
/usr/include/telepathy-qt5/TelepathyQt/CallStreamEndpointInterface
/usr/include/telepathy-qt5/TelepathyQt/CallStreamInterface
/usr/include/telepathy-qt5/TelepathyQt/CallStreamInterfaceMediaInterface
/usr/include/telepathy-qt5/TelepathyQt/Callbacks
/usr/include/telepathy-qt5/TelepathyQt/CapabilitiesBase
/usr/include/telepathy-qt5/TelepathyQt/Captcha
/usr/include/telepathy-qt5/TelepathyQt/CaptchaAuthentication
/usr/include/telepathy-qt5/TelepathyQt/Channel
/usr/include/telepathy-qt5/TelepathyQt/ChannelClassFeatures
/usr/include/telepathy-qt5/TelepathyQt/ChannelClassSpec
/usr/include/telepathy-qt5/TelepathyQt/ChannelClassSpecList
/usr/include/telepathy-qt5/TelepathyQt/ChannelDispatchOperation
/usr/include/telepathy-qt5/TelepathyQt/ChannelDispatchOperationInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelDispatcher
/usr/include/telepathy-qt5/TelepathyQt/ChannelDispatcherInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelFactory
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceAnonymityInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceCallStateInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceCaptchaAuthenticationInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceChatStateInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceConferenceInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceDTMFInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceDestroyableInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceFileTransferMetadataInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceGroupInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceHoldInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceMediaSignallingInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceMessagesInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfacePasswordInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceRoomConfigInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceRoomInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceSASLAuthenticationInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceSMSInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceSecurableInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceServicePointInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceSubjectInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelInterfaceTubeInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelRequest
/usr/include/telepathy-qt5/TelepathyQt/ChannelRequestHints
/usr/include/telepathy-qt5/TelepathyQt/ChannelRequestInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeCallInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeContactListInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeContactSearchInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeDBusTubeInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeFileTransferInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeRoomListInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeServerAuthenticationInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeServerTLSConnectionInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeStreamTubeInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeStreamedMediaInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeTextInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeTubeInterface
/usr/include/telepathy-qt5/TelepathyQt/ChannelTypeTubesInterface
/usr/include/telepathy-qt5/TelepathyQt/Client
/usr/include/telepathy-qt5/TelepathyQt/ClientApproverInterface
/usr/include/telepathy-qt5/TelepathyQt/ClientHandlerInterface
/usr/include/telepathy-qt5/TelepathyQt/ClientInterface
/usr/include/telepathy-qt5/TelepathyQt/ClientInterfaceRequestsInterface
/usr/include/telepathy-qt5/TelepathyQt/ClientObserverInterface
/usr/include/telepathy-qt5/TelepathyQt/ClientRegistrar
/usr/include/telepathy-qt5/TelepathyQt/Connection
/usr/include/telepathy-qt5/TelepathyQt/ConnectionCapabilities
/usr/include/telepathy-qt5/TelepathyQt/ConnectionFactory
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceAddressingInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceAliasingInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceAnonymityInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceAvatarsInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceBalanceInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceCapabilitiesInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceCellularInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceClientTypesInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceContactBlockingInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceContactCapabilitiesInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceContactGroupsInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceContactInfoInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceContactListInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceContactsInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceLocationInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceMailNotificationInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfacePowerSavingInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfacePresenceInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceRequestsInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceServicePointInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionInterfaceSimplePresenceInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionLowlevel
/usr/include/telepathy-qt5/TelepathyQt/ConnectionManager
/usr/include/telepathy-qt5/TelepathyQt/ConnectionManagerInterface
/usr/include/telepathy-qt5/TelepathyQt/ConnectionManagerLowlevel
/usr/include/telepathy-qt5/TelepathyQt/Constants
/usr/include/telepathy-qt5/TelepathyQt/Contact
/usr/include/telepathy-qt5/TelepathyQt/ContactCapabilities
/usr/include/telepathy-qt5/TelepathyQt/ContactFactory
/usr/include/telepathy-qt5/TelepathyQt/ContactManager
/usr/include/telepathy-qt5/TelepathyQt/ContactMessenger
/usr/include/telepathy-qt5/TelepathyQt/ContactSearchChannel
/usr/include/telepathy-qt5/TelepathyQt/DBus
/usr/include/telepathy-qt5/TelepathyQt/DBusDaemonInterface
/usr/include/telepathy-qt5/TelepathyQt/DBusError
/usr/include/telepathy-qt5/TelepathyQt/DBusObject
/usr/include/telepathy-qt5/TelepathyQt/DBusProxy
/usr/include/telepathy-qt5/TelepathyQt/DBusProxyFactory
/usr/include/telepathy-qt5/TelepathyQt/DBusService
/usr/include/telepathy-qt5/TelepathyQt/DBusTubeChannel
/usr/include/telepathy-qt5/TelepathyQt/Debug
/usr/include/telepathy-qt5/TelepathyQt/DebugReceiver
/usr/include/telepathy-qt5/TelepathyQt/Feature
/usr/include/telepathy-qt5/TelepathyQt/Features
/usr/include/telepathy-qt5/TelepathyQt/FileTransferChannel
/usr/include/telepathy-qt5/TelepathyQt/FileTransferChannelCreationProperties
/usr/include/telepathy-qt5/TelepathyQt/Filter
/usr/include/telepathy-qt5/TelepathyQt/FixedFeatureFactory
/usr/include/telepathy-qt5/TelepathyQt/Functors
/usr/include/telepathy-qt5/TelepathyQt/GenericCapabilityFilter
/usr/include/telepathy-qt5/TelepathyQt/GenericPropertyFilter
/usr/include/telepathy-qt5/TelepathyQt/Global
/usr/include/telepathy-qt5/TelepathyQt/HandledChannelNotifier
/usr/include/telepathy-qt5/TelepathyQt/IODevice
/usr/include/telepathy-qt5/TelepathyQt/IncomingDBusTubeChannel
/usr/include/telepathy-qt5/TelepathyQt/IncomingFileTransferChannel
/usr/include/telepathy-qt5/TelepathyQt/IncomingStreamTubeChannel
/usr/include/telepathy-qt5/TelepathyQt/IntrospectableInterface
/usr/include/telepathy-qt5/TelepathyQt/LocationInfo
/usr/include/telepathy-qt5/TelepathyQt/MediaSessionHandler
/usr/include/telepathy-qt5/TelepathyQt/MediaSessionHandlerInterface
/usr/include/telepathy-qt5/TelepathyQt/MediaStreamHandler
/usr/include/telepathy-qt5/TelepathyQt/MediaStreamHandlerInterface
/usr/include/telepathy-qt5/TelepathyQt/Message
/usr/include/telepathy-qt5/TelepathyQt/MessageContentPart
/usr/include/telepathy-qt5/TelepathyQt/MessageContentPartList
/usr/include/telepathy-qt5/TelepathyQt/MethodInvocationContext
/usr/include/telepathy-qt5/TelepathyQt/NotFilter
/usr/include/telepathy-qt5/TelepathyQt/Object
/usr/include/telepathy-qt5/TelepathyQt/OptionalInterfaceFactory
/usr/include/telepathy-qt5/TelepathyQt/OrFilter
/usr/include/telepathy-qt5/TelepathyQt/OutgoingDBusTubeChannel
/usr/include/telepathy-qt5/TelepathyQt/OutgoingFileTransferChannel
/usr/include/telepathy-qt5/TelepathyQt/OutgoingStreamTubeChannel
/usr/include/telepathy-qt5/TelepathyQt/PeerInterface
/usr/include/telepathy-qt5/TelepathyQt/PendingAccount
/usr/include/telepathy-qt5/TelepathyQt/PendingCallContent
/usr/include/telepathy-qt5/TelepathyQt/PendingCaptchas
/usr/include/telepathy-qt5/TelepathyQt/PendingChannel
/usr/include/telepathy-qt5/TelepathyQt/PendingChannelRequest
/usr/include/telepathy-qt5/TelepathyQt/PendingComposite
/usr/include/telepathy-qt5/TelepathyQt/PendingConnection
/usr/include/telepathy-qt5/TelepathyQt/PendingContactAttributes
/usr/include/telepathy-qt5/TelepathyQt/PendingContactInfo
/usr/include/telepathy-qt5/TelepathyQt/PendingContacts
/usr/include/telepathy-qt5/TelepathyQt/PendingDBusTubeConnection
/usr/include/telepathy-qt5/TelepathyQt/PendingDebugMessageList
/usr/include/telepathy-qt5/TelepathyQt/PendingFailure
/usr/include/telepathy-qt5/TelepathyQt/PendingHandles
/usr/include/telepathy-qt5/TelepathyQt/PendingOperation
/usr/include/telepathy-qt5/TelepathyQt/PendingReady
/usr/include/telepathy-qt5/TelepathyQt/PendingSendMessage
/usr/include/telepathy-qt5/TelepathyQt/PendingStreamTubeConnection
/usr/include/telepathy-qt5/TelepathyQt/PendingStreamedMediaStreams
/usr/include/telepathy-qt5/TelepathyQt/PendingString
/usr/include/telepathy-qt5/TelepathyQt/PendingStringList
/usr/include/telepathy-qt5/TelepathyQt/PendingSuccess
/usr/include/telepathy-qt5/TelepathyQt/PendingVariant
/usr/include/telepathy-qt5/TelepathyQt/PendingVariantMap
/usr/include/telepathy-qt5/TelepathyQt/PendingVoid
/usr/include/telepathy-qt5/TelepathyQt/Presence
/usr/include/telepathy-qt5/TelepathyQt/PresenceSpec
/usr/include/telepathy-qt5/TelepathyQt/PresenceSpecList
/usr/include/telepathy-qt5/TelepathyQt/Profile
/usr/include/telepathy-qt5/TelepathyQt/ProfileManager
/usr/include/telepathy-qt5/TelepathyQt/Properties
/usr/include/telepathy-qt5/TelepathyQt/PropertiesInterface
/usr/include/telepathy-qt5/TelepathyQt/PropertiesInterfaceInterface
/usr/include/telepathy-qt5/TelepathyQt/ProtocolInfo
/usr/include/telepathy-qt5/TelepathyQt/ProtocolInfoList
/usr/include/telepathy-qt5/TelepathyQt/ProtocolInterface
/usr/include/telepathy-qt5/TelepathyQt/ProtocolInterfaceAddressingInterface
/usr/include/telepathy-qt5/TelepathyQt/ProtocolInterfaceAvatarsInterface
/usr/include/telepathy-qt5/TelepathyQt/ProtocolInterfacePresenceInterface
/usr/include/telepathy-qt5/TelepathyQt/ProtocolParameter
/usr/include/telepathy-qt5/TelepathyQt/ProtocolParameterList
/usr/include/telepathy-qt5/TelepathyQt/ReadinessHelper
/usr/include/telepathy-qt5/TelepathyQt/ReadyObject
/usr/include/telepathy-qt5/TelepathyQt/ReceivedMessage
/usr/include/telepathy-qt5/TelepathyQt/RefCounted
/usr/include/telepathy-qt5/TelepathyQt/ReferencedHandles
/usr/include/telepathy-qt5/TelepathyQt/ReferencedHandlesIterator
/usr/include/telepathy-qt5/TelepathyQt/RequestableChannelClassSpec
/usr/include/telepathy-qt5/TelepathyQt/RequestableChannelClassSpecList
/usr/include/telepathy-qt5/TelepathyQt/RoomListChannel
/usr/include/telepathy-qt5/TelepathyQt/ServerAuthenticationChannel
/usr/include/telepathy-qt5/TelepathyQt/ServiceTypes
/usr/include/telepathy-qt5/TelepathyQt/SharedPtr
/usr/include/telepathy-qt5/TelepathyQt/SimpleCallObserver
/usr/include/telepathy-qt5/TelepathyQt/SimpleObserver
/usr/include/telepathy-qt5/TelepathyQt/SimpleTextObserver
/usr/include/telepathy-qt5/TelepathyQt/StatefulDBusProxy
/usr/include/telepathy-qt5/TelepathyQt/StatelessDBusProxy
/usr/include/telepathy-qt5/TelepathyQt/StreamTubeChannel
/usr/include/telepathy-qt5/TelepathyQt/StreamTubeClient
/usr/include/telepathy-qt5/TelepathyQt/StreamTubeServer
/usr/include/telepathy-qt5/TelepathyQt/StreamedMediaChannel
/usr/include/telepathy-qt5/TelepathyQt/StreamedMediaStream
/usr/include/telepathy-qt5/TelepathyQt/TextChannel
/usr/include/telepathy-qt5/TelepathyQt/TubeChannel
/usr/include/telepathy-qt5/TelepathyQt/Types
/usr/include/telepathy-qt5/TelepathyQt/Utils
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-account-manager.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-account.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-call-content-media-description.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-call-content.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-call-stream-endpoint.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-call-stream.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-channel-dispatch-operation.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-channel-dispatcher.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-channel-request.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-channel.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-client.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-connection-manager.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-connection.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-dbus.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-debug-receiver.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-media-session-handler.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-media-stream-handler.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-properties.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/cli-tls-certificate.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/constants.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/svc-call.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/svc-channel.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/svc-connection-manager.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/svc-connection.h
/usr/include/telepathy-qt5/TelepathyQt/_gen/types.h
/usr/include/telepathy-qt5/TelepathyQt/abstract-adaptor.h
/usr/include/telepathy-qt5/TelepathyQt/abstract-client.h
/usr/include/telepathy-qt5/TelepathyQt/abstract-interface.h
/usr/include/telepathy-qt5/TelepathyQt/account-capability-filter.h
/usr/include/telepathy-qt5/TelepathyQt/account-factory.h
/usr/include/telepathy-qt5/TelepathyQt/account-filter.h
/usr/include/telepathy-qt5/TelepathyQt/account-manager.h
/usr/include/telepathy-qt5/TelepathyQt/account-property-filter.h
/usr/include/telepathy-qt5/TelepathyQt/account-set.h
/usr/include/telepathy-qt5/TelepathyQt/account.h
/usr/include/telepathy-qt5/TelepathyQt/and-filter.h
/usr/include/telepathy-qt5/TelepathyQt/avatar.h
/usr/include/telepathy-qt5/TelepathyQt/base-call.h
/usr/include/telepathy-qt5/TelepathyQt/base-channel.h
/usr/include/telepathy-qt5/TelepathyQt/base-connection-manager.h
/usr/include/telepathy-qt5/TelepathyQt/base-connection.h
/usr/include/telepathy-qt5/TelepathyQt/base-debug.h
/usr/include/telepathy-qt5/TelepathyQt/base-protocol.h
/usr/include/telepathy-qt5/TelepathyQt/call-channel.h
/usr/include/telepathy-qt5/TelepathyQt/call-content-media-description.h
/usr/include/telepathy-qt5/TelepathyQt/call-content.h
/usr/include/telepathy-qt5/TelepathyQt/call-stream-endpoint.h
/usr/include/telepathy-qt5/TelepathyQt/call-stream.h
/usr/include/telepathy-qt5/TelepathyQt/callbacks.h
/usr/include/telepathy-qt5/TelepathyQt/capabilities-base.h
/usr/include/telepathy-qt5/TelepathyQt/captcha-authentication.h
/usr/include/telepathy-qt5/TelepathyQt/captcha.h
/usr/include/telepathy-qt5/TelepathyQt/channel-class-features.h
/usr/include/telepathy-qt5/TelepathyQt/channel-class-spec.h
/usr/include/telepathy-qt5/TelepathyQt/channel-dispatch-operation.h
/usr/include/telepathy-qt5/TelepathyQt/channel-dispatcher.h
/usr/include/telepathy-qt5/TelepathyQt/channel-factory.h
/usr/include/telepathy-qt5/TelepathyQt/channel-request.h
/usr/include/telepathy-qt5/TelepathyQt/channel.h
/usr/include/telepathy-qt5/TelepathyQt/client-registrar.h
/usr/include/telepathy-qt5/TelepathyQt/client.h
/usr/include/telepathy-qt5/TelepathyQt/connection-capabilities.h
/usr/include/telepathy-qt5/TelepathyQt/connection-factory.h
/usr/include/telepathy-qt5/TelepathyQt/connection-lowlevel.h
/usr/include/telepathy-qt5/TelepathyQt/connection-manager-lowlevel.h
/usr/include/telepathy-qt5/TelepathyQt/connection-manager.h
/usr/include/telepathy-qt5/TelepathyQt/connection.h
/usr/include/telepathy-qt5/TelepathyQt/constants.h
/usr/include/telepathy-qt5/TelepathyQt/contact-capabilities.h
/usr/include/telepathy-qt5/TelepathyQt/contact-factory.h
/usr/include/telepathy-qt5/TelepathyQt/contact-manager.h
/usr/include/telepathy-qt5/TelepathyQt/contact-messenger.h
/usr/include/telepathy-qt5/TelepathyQt/contact-search-channel.h
/usr/include/telepathy-qt5/TelepathyQt/contact.h
/usr/include/telepathy-qt5/TelepathyQt/dbus-error.h
/usr/include/telepathy-qt5/TelepathyQt/dbus-object.h
/usr/include/telepathy-qt5/TelepathyQt/dbus-proxy-factory.h
/usr/include/telepathy-qt5/TelepathyQt/dbus-proxy.h
/usr/include/telepathy-qt5/TelepathyQt/dbus-service.h
/usr/include/telepathy-qt5/TelepathyQt/dbus-tube-channel.h
/usr/include/telepathy-qt5/TelepathyQt/dbus.h
/usr/include/telepathy-qt5/TelepathyQt/debug-receiver.h
/usr/include/telepathy-qt5/TelepathyQt/debug.h
/usr/include/telepathy-qt5/TelepathyQt/feature.h
/usr/include/telepathy-qt5/TelepathyQt/file-transfer-channel-creation-properties.h
/usr/include/telepathy-qt5/TelepathyQt/file-transfer-channel.h
/usr/include/telepathy-qt5/TelepathyQt/filter.h
/usr/include/telepathy-qt5/TelepathyQt/fixed-feature-factory.h
/usr/include/telepathy-qt5/TelepathyQt/functors.h
/usr/include/telepathy-qt5/TelepathyQt/generic-capability-filter.h
/usr/include/telepathy-qt5/TelepathyQt/generic-property-filter.h
/usr/include/telepathy-qt5/TelepathyQt/global.h
/usr/include/telepathy-qt5/TelepathyQt/handled-channel-notifier.h
/usr/include/telepathy-qt5/TelepathyQt/incoming-dbus-tube-channel.h
/usr/include/telepathy-qt5/TelepathyQt/incoming-file-transfer-channel.h
/usr/include/telepathy-qt5/TelepathyQt/incoming-stream-tube-channel.h
/usr/include/telepathy-qt5/TelepathyQt/io-device.h
/usr/include/telepathy-qt5/TelepathyQt/location-info.h
/usr/include/telepathy-qt5/TelepathyQt/media-session-handler.h
/usr/include/telepathy-qt5/TelepathyQt/media-stream-handler.h
/usr/include/telepathy-qt5/TelepathyQt/message-content-part.h
/usr/include/telepathy-qt5/TelepathyQt/message.h
/usr/include/telepathy-qt5/TelepathyQt/method-invocation-context.h
/usr/include/telepathy-qt5/TelepathyQt/not-filter.h
/usr/include/telepathy-qt5/TelepathyQt/object.h
/usr/include/telepathy-qt5/TelepathyQt/optional-interface-factory.h
/usr/include/telepathy-qt5/TelepathyQt/or-filter.h
/usr/include/telepathy-qt5/TelepathyQt/outgoing-dbus-tube-channel.h
/usr/include/telepathy-qt5/TelepathyQt/outgoing-file-transfer-channel.h
/usr/include/telepathy-qt5/TelepathyQt/outgoing-stream-tube-channel.h
/usr/include/telepathy-qt5/TelepathyQt/pending-account.h
/usr/include/telepathy-qt5/TelepathyQt/pending-captchas.h
/usr/include/telepathy-qt5/TelepathyQt/pending-channel-request.h
/usr/include/telepathy-qt5/TelepathyQt/pending-channel.h
/usr/include/telepathy-qt5/TelepathyQt/pending-connection.h
/usr/include/telepathy-qt5/TelepathyQt/pending-contact-attributes.h
/usr/include/telepathy-qt5/TelepathyQt/pending-contact-info.h
/usr/include/telepathy-qt5/TelepathyQt/pending-contacts.h
/usr/include/telepathy-qt5/TelepathyQt/pending-dbus-tube-connection.h
/usr/include/telepathy-qt5/TelepathyQt/pending-debug-message-list.h
/usr/include/telepathy-qt5/TelepathyQt/pending-handles.h
/usr/include/telepathy-qt5/TelepathyQt/pending-operation.h
/usr/include/telepathy-qt5/TelepathyQt/pending-ready.h
/usr/include/telepathy-qt5/TelepathyQt/pending-send-message.h
/usr/include/telepathy-qt5/TelepathyQt/pending-stream-tube-connection.h
/usr/include/telepathy-qt5/TelepathyQt/pending-string-list.h
/usr/include/telepathy-qt5/TelepathyQt/pending-string.h
/usr/include/telepathy-qt5/TelepathyQt/pending-variant-map.h
/usr/include/telepathy-qt5/TelepathyQt/pending-variant.h
/usr/include/telepathy-qt5/TelepathyQt/presence.h
/usr/include/telepathy-qt5/TelepathyQt/profile-manager.h
/usr/include/telepathy-qt5/TelepathyQt/profile.h
/usr/include/telepathy-qt5/TelepathyQt/properties.h
/usr/include/telepathy-qt5/TelepathyQt/protocol-info.h
/usr/include/telepathy-qt5/TelepathyQt/protocol-parameter.h
/usr/include/telepathy-qt5/TelepathyQt/readiness-helper.h
/usr/include/telepathy-qt5/TelepathyQt/ready-object.h
/usr/include/telepathy-qt5/TelepathyQt/referenced-handles.h
/usr/include/telepathy-qt5/TelepathyQt/requestable-channel-class-spec.h
/usr/include/telepathy-qt5/TelepathyQt/room-list-channel.h
/usr/include/telepathy-qt5/TelepathyQt/server-authentication-channel.h
/usr/include/telepathy-qt5/TelepathyQt/service-types.h
/usr/include/telepathy-qt5/TelepathyQt/shared-ptr.h
/usr/include/telepathy-qt5/TelepathyQt/simple-call-observer.h
/usr/include/telepathy-qt5/TelepathyQt/simple-observer.h
/usr/include/telepathy-qt5/TelepathyQt/simple-pending-operations.h
/usr/include/telepathy-qt5/TelepathyQt/simple-text-observer.h
/usr/include/telepathy-qt5/TelepathyQt/stream-tube-channel.h
/usr/include/telepathy-qt5/TelepathyQt/stream-tube-client.h
/usr/include/telepathy-qt5/TelepathyQt/stream-tube-server.h
/usr/include/telepathy-qt5/TelepathyQt/streamed-media-channel.h
/usr/include/telepathy-qt5/TelepathyQt/text-channel.h
/usr/include/telepathy-qt5/TelepathyQt/tls-certificate.h
/usr/include/telepathy-qt5/TelepathyQt/tube-channel.h
/usr/include/telepathy-qt5/TelepathyQt/types.h
/usr/include/telepathy-qt5/TelepathyQt/utils.h
/usr/lib64/cmake/TelepathyQt5/TelepathyQt5Config.cmake
/usr/lib64/cmake/TelepathyQt5/TelepathyQt5ConfigVersion.cmake
/usr/lib64/cmake/TelepathyQt5/TelepathyQt5Targets-relwithdebinfo.cmake
/usr/lib64/cmake/TelepathyQt5/TelepathyQt5Targets.cmake
/usr/lib64/cmake/TelepathyQt5Service/TelepathyQt5ServiceConfig.cmake
/usr/lib64/cmake/TelepathyQt5Service/TelepathyQt5ServiceConfigVersion.cmake
/usr/lib64/libtelepathy-qt5-service.so
/usr/lib64/libtelepathy-qt5.so
/usr/lib64/pkgconfig/TelepathyQt5.pc
/usr/lib64/pkgconfig/TelepathyQt5Service.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtelepathy-qt5-service.so.0
/usr/lib64/libtelepathy-qt5-service.so.0.0.9.7
/usr/lib64/libtelepathy-qt5.so.0
/usr/lib64/libtelepathy-qt5.so.0.0.9.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/telepathy-qt/9a1929f4700d2407c70b507b3b2aaf6226a9543c
