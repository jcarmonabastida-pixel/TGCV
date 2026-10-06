package org.tgcv.viatra.v002.observer;

import org.eclipse.emf.ecore.EObject;
import org.eclipse.viatra.query.patternlanguage.emf.EMFPatternLanguageStandaloneSetup;
import org.eclipse.viatra.query.patternlanguage.emf.util.IClassLoaderProvider;

import com.google.inject.Guice;
import com.google.inject.Injector;

/**
 * VIATRA 2.0.2 standalone parser setup with the observer bundle classloader.
 */
public final class ObserverPatternParserSetup extends EMFPatternLanguageStandaloneSetup {

    public Injector createObserverInjector() {
        Injector injector = Guice.createInjector(new ObserverParserModule());
        register(injector);
        return injector;
    }

    public static final class ObserverParserModule extends StandaloneParserModule {
        @Override
        public Class<? extends IClassLoaderProvider> bindIClassLoaderProvider() {
            return ObserverClassLoaderProvider.class;
        }
    }

    public static final class ObserverClassLoaderProvider
            implements IClassLoaderProvider {
        @Override
        public ClassLoader getClassLoader(EObject context) {
            ClassLoader loader = ObserverPatternParserSetup.class.getClassLoader();
            if (loader == null) {
                throw new IllegalStateException(
                    "Observer bundle classloader is unavailable");
            }
            return loader;
        }
    }
}
