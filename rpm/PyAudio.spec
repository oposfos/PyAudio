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
%setup -q -n PyAudio-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}


%files
%doc CHANGELOG README
%doc examples/
%{python_sitearch}/_portaudio*.so
%{python_sitearch}/pyaudio.py*
%pycache_only %{python_sitearch}/__pycache__/pyaudio*.py*
%{python_sitearch}/PyAudio-%{version}-py*.egg-info
