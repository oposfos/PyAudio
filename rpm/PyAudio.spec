Name:           PyAudio
Version:        0.2.14
Release:        0
Summary:        Python Bindings for PortAudio v19
License:        MIT
URL:            https://people.csail.mit.edu/hubert/pyaudio/
Source:         https://files.pythonhosted.org/packages/source/P/PyAudio/PyAudio-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  fdupes
BuildRequires:  portaudio-devel
BuildRequires:  python-rpm-macros

%description
PyAudio provides Python bindings for PortAudio v19, the cross-platform audio I/O library.
With PyAudio, you can easily use Python to play and record audio streams on a variety
of platforms (e.g., GNU/Linux, Microsoft Windows, and Mac OS X).

%prep
%autosetup -n %{name}-%{version}

%build
tar -xvf %{name}-%{version}.tar.gz
cd %{name}-%{version}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%py3_build

%install
rm -rf %{buildroot}
cd %{name}-%{version}
%py3_install


%files
%{python3_sitearch}/pyaudio
%{python3_sitearch}/PyAudio-%{version}-py%{python3_version}.egg-info
