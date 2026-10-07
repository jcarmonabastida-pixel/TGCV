package org.tgcv.viatra.v002.observer;

import java.io.InputStream;
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
        System.out.println("TGCV_CREATE_INJECTOR_DIAGNOSTIC=beforeGuiceCreateInjector");
        Injector injector = Guice.createInjector(new ObserverParserModule());
        register(injector);
        return injector;
    }

    public static final class ObserverParserModule extends StandaloneParserModule {
        @Override
        public Class<? extends IClassLoaderProvider> bindIClassLoaderProvider() {
            return ObserverClassLoaderProvider.class;
        }

        @Override
        public void configure() {
            super.configure();
            org.eclipse.xtext.resource.XtextResourceSet rs = new org.eclipse.xtext.resource.XtextResourceSet();
            org.eclipse.emf.ecore.resource.Resource.Factory.Registry registry = rs.getResourceFactoryRegistry();
            System.out.println("TGCV_XTEXT_FACTORY_DIAGNOSTIC=xtextbin=" + registry.getExtensionToFactoryMap().get("xtextbin"));
            System.out.println("TGCV_XTEXT_FACTORY_DIAGNOSTIC=ecore=" + registry.getExtensionToFactoryMap().get("ecore"));
            System.out.println("TGCV_XTEXT_FACTORY_DIAGNOSTIC=xmi=" + registry.getExtensionToFactoryMap().get("xmi"));
            System.out.println("TGCV_XTEXT_FACTORY_DIAGNOSTIC=registryClass=" + registry.getClass().getName());
            System.out.println("TGCV_XTEXT_FACTORY_DIAGNOSTIC=xtextbinFactoryClass=" +
                (registry.getExtensionToFactoryMap().get("xtextbin") == null ? "null" :
                    registry.getExtensionToFactoryMap().get("xtextbin").getClass().getName()));
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

            String resourceName = "org/eclipse/xtext/xbase/Xtype.xtextbin";
            System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=loader=" + loader.getClass().getName());
            System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=loaderToString=" + loader);
            System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=resource=" + resourceName);
            java.net.URL resource = loader.getResource(resourceName);
            System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=resourceUrl=" + resource);

            if (resource != null) {
                try (InputStream in = resource.openStream()) {
                    byte[] head = new byte[16];
                    int n = in.read(head);
                    StringBuilder hex = new StringBuilder();
                    for (int i = 0; i < n; i++) {
                        if (i > 0) {
                            hex.append(' ');
                        }
                        hex.append(String.format("%02x", head[i] & 0xff));
                    }
                    System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=resourceHead=" + hex);
                } catch (Exception e) {
                    System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=resourceReadError=" +
                        e.getClass().getName() + ":" + e.getMessage());
                }
            }

            return loader;
        }
    }
}
