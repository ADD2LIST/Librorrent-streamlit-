import streamlit as st
import libtorrent as lt

def download_torrent(magnet_link):
    ses = lt.session()
    params = {
        'save_path': '.',  # Set the save path for the downloaded torrent file
        'storage_mode': lt.storage_mode_t(2),
        'paused': False,
        'auto_managed': True,
        'duplicate_is_error': True
    }
    handle = lt.add_magnet_uri(ses, magnet_link, params)
    ses.start_dht()

    while not handle.has_metadata():
        pass

    info = handle.get_torrent_info()
    file_path = info.name()
    st.write("Downloading:", file_path)

    while handle.status().state != lt.torrent_status.seeding:
        st.write("Progress:", handle.status().progress * 100)
        lt.sleep(1)

    st.write("Download complete:", file_path)


def main():
    st.title("Torrent Downloader")

    # Search Form
    st.subheader("Search Torrents")
    query = st.text_input("Enter the torrent you want to search:")
    search_button = st.button("Search")

    if search_button:
        if query:
            # Perform search and display results
            st.info(f"Searching for {query}...")
            # ... perform the search logic here and get the results ...
            # ... store the results in a variable called `results` ...

            # Example results (replace with your own logic)
            results = [
                {'Name': 'Torrent 1', 'Magnet': 'magnet link 1'},
                {'Name': 'Torrent 2', 'Magnet': 'magnet link 2'},
                {'Name': 'Torrent 3', 'Magnet': 'magnet link 3'}
            ]

            if results:
                st.success(f"Found {len(results)} torrents.")
                st.markdown("---")
                for torrent in results:
                    st.write("Name:", torrent['Name'])
                    st.write("Magnet Link:", torrent['Magnet'])
                    download_button = st.button("Download", key=torrent['Magnet'])
                    if download_button:
                        download_torrent(torrent['Magnet'])
                    st.markdown("---")
            else:
                st.warning("No torrents found.")
        else:
            st.warning("Please enter a search query.")

    # Instructions
    st.subheader("Instructions")
    st.write("1. Enter a search query to search for torrents.")
    st.write("2. Click the 'Search' button to perform the search.")
    st.write("3. The search results will be displayed below.")
    st.write("4. Click the 'Download' button next to a torrent to start the download.")

if __name__ == "__main__":
    main()
  
